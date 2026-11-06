// Events inquiry -> email to the events team via Resend (https://resend.com).
// Vercel environment variables:
//   RESEND_API_KEY  (required)  API key from resend.com
//   INQUIRY_TO      (optional)  defaults to yervand@ikitoro.com
//   INQUIRY_FROM    (optional)  e.g. "Iki Toro Website <events@ikitoro.com>" once ikitoro.com
//                               is verified in Resend; defaults to Resend's test sender, which
//                               can only deliver to the email that owns the Resend account.
const FIELDS = ["Occasion", "Date", "Guests", "Name", "Company", "Email", "Phone", "Notes"];
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

module.exports = async (req, res) => {
  if (req.method !== "POST") { res.setHeader("Allow", "POST"); return res.status(405).json({ success: false, message: "Use POST" }); }
  let body = req.body;
  if (typeof body === "string") { try { body = JSON.parse(body); } catch { body = {}; } }
  body = body || {};
  if (body._honey) return res.status(200).json({ success: true }); // spam bot

  const clean = v => String(v == null ? "" : v).slice(0, 2000).trim();
  const data = {}; for (const k of FIELDS) data[k] = clean(body[k]);
  if (!data.Name || !data.Date || !/^\S+@\S+\.\S+$/.test(data.Email)) {
    return res.status(400).json({ success: false, message: "Missing name, date or a valid email" });
  }

  const key = process.env.RESEND_API_KEY;
  if (!key) { console.error("RESEND_API_KEY is not set"); return res.status(503).json({ success: false, message: "Email is not configured yet" }); }

  const subject = `Event inquiry: ${data.Occasion || "Event"}, ${data.Date}, ${data.Guests || "?"} guests`;
  const rows = FIELDS.map(k => `<tr><td style="padding:8px 14px;border-bottom:1px solid #eee;color:#777;font:13px Georgia,serif">${k}</td><td style="padding:8px 14px;border-bottom:1px solid #eee;font:15px Georgia,serif;white-space:pre-wrap">${esc(data[k] || "—")}</td></tr>`).join("");
  const html = `<div style="max-width:560px"><h2 style="font:400 22px Georgia,serif;color:#47042b">New event inquiry</h2><table style="border-collapse:collapse;width:100%">${rows}</table><p style="font:13px Georgia,serif;color:#777">Sent from the events form on the Iki Toro website. Reply to this email to answer the guest directly.</p></div>`;
  const text = FIELDS.map(k => `${k}: ${data[k] || "—"}`).join("\n");

  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        from: process.env.INQUIRY_FROM || "Iki Toro Website <onboarding@resend.dev>",
        to: [process.env.INQUIRY_TO || "yervand@ikitoro.com"],
        reply_to: data.Email,
        subject, html, text,
      }),
    });
    const out = await r.json().catch(() => ({}));
    if (!r.ok) { console.error("Resend rejected inquiry:", r.status, JSON.stringify(out).slice(0, 300)); return res.status(502).json({ success: false, message: out.message || `Resend HTTP ${r.status}` }); }
    return res.status(200).json({ success: true, id: out.id });
  } catch (err) {
    console.error("Resend unreachable:", err && err.message);
    return res.status(502).json({ success: false, message: "Email service unreachable" });
  }
};
