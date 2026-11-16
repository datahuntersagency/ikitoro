# Iki Toro — website

Static site for Iki Toro, Japanese fine dining at 120 S Brand Blvd, Glendale.

- `index.html` — the whole site (HTML, CSS and JS in one file)
- `assets/` — logo and favicon
- `menus/` — the four menu PDFs and their page images
- `api/inquiry.js` — emails event inquiries via Resend (needs `RESEND_API_KEY`, optional `INQUIRY_FROM` / `INQUIRY_TO`)

## Instagram
The Journal slider loads the latest posts and reels from the Behold feed set in
`INSTAGRAM_FEED_URL` near the top of the script in `index.html`.

## Hours
Edit the `HOURS` object in the script (minutes after midnight, Pacific time).
Weekend lunch from 12 pm; Sunset Omakase ($70 omakase-style prix fixe) 5–6 pm daily.

## Deploy
Static, no build step. Import the repo in Vercel with framework preset "Other";
every push to `main` redeploys.
