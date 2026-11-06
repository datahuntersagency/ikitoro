// Events inquiry relay: the browser posts here (same origin, no CORS),
// and this function forwards the inquiry to FormSubmit server-side.
const INQUIRY_EMAIL = "yervand@ikitoro.com";
const FIELDS = ["Occasion", "Date", "Guests", "Name", "Company", "Email", "Phone", "Notes"];

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ success: false, message: "Use POST" });
  }
  let body = req.body;
  if (typeof body === "string") { try { body = JSON.parse(body); } catch { body = {}; } }
  body = body || {};

  if (body._honey) return res.status(200).json({ success: true }); // spam bot
  const clean = v => String(v == null ? "" : v).slice(0, 2000).trim();
  const email = clean(body.Email);
  if (!clean(body.Name) || !clean(body.Date) || !/^\S+@\S+\.\S+$/.test(email)) {
    return res.status(400).json({ success: false, message: "Missing name, date or a valid email" });
  }

  const payload = {
    _subject: clean(body._subject) || "Event inquiry",
    _template: "table",
    _replyto: email,
    _captcha: "false",
  };
  for (const k of FIELDS) payload[k] = clean(body[k]) || "—";

  const site = `https://${req.headers["x-forwarded-host"] || req.headers.host || "ikitoro.vercel.app"}`;
  try {
    const r = await fetch(`https://formsubmit.co/ajax/${INQUIRY_EMAIL}`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json", Origin: site, Referer: site + "/" },
      body: JSON.stringify(payload),
    });
    const text = await r.text();
    let j = {}; try { j = JSON.parse(text); } catch {}
    const ok = r.ok && j.success !== false && j.success !== "false";
    if (!ok) console.error("FormSubmit rejected inquiry:", r.status, text.slice(0, 300));
    return res.status(ok ? 200 : 502).json({ success: ok, message: j.message || (ok ? "sent" : `FormSubmit HTTP ${r.status}`) });
  } catch (err) {
    console.error("FormSubmit unreachable:", err && err.message);
    return res.status(502).json({ success: false, message: "Email service unreachable" });
  }
};
