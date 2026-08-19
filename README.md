# jamesnightingale.net

Static site for [James Nightingale](https://jamesnightingale.net), served by GitHub Pages.

## Provenance

Ported from the WordPress site (Twenty Sixteen theme) that ran on HostGator,
using the mirror captured on 2026-08-14 in `~/backups/jamesnightingale.net/`.
The markup is the original WordPress output, kept as-is. Changes made during the port:

- Menu links rewritten from `?p=NNNN` permalinks to the directory URLs (`/cv/`, `/publications/`, …).
- Removed WordPress endpoints with no static equivalent: `wp-admin/`, `wp-json/`,
  `feed/`, `comments/`, `xmlrpc`, `wp-login`, and the duplicate `?p=` page copies.
- Removed the emoji-loader script and oEmbed/RSD `<link>` tags, which pointed at the old host.
- Google Fonts (vendored under `fonts.googleapis.com/` and `fonts.gstatic.com/`)
  re-based to root-absolute paths.

Verified after porting: all 8 pages and 347 assets serve 200 with no broken references,
and the visible text of every page matches the live WordPress site.

## Editing

Pages are plain HTML — edit the relevant `index.html` and push:

| URL | File |
|-----|------|
| `/` | `index.html` |
| `/cv/` | `cv/index.html` |
| `/publications/` | `publications/index.html` |
| `/talks/` | `talks/index.html` |
| `/cancer/` | `cancer/index.html` |
| `/cosmology/` | `cosmology/index.html` |
| `/euclid/` | `euclid/index.html` |
| `/contact/` | `contact/index.html` |

The page body sits inside `<div class="entry-content">`; everything around it is
theme chrome, repeated in each file. Uploads (images, PDFs, slides) live under
`wp-content/uploads/` and can be linked directly.

`.nojekyll` is required — it stops GitHub Pages running Jekyll, which would
mishandle the `wp-content` directory and the `@ver=` asset filenames.

## Local preview

```bash
python3 -m http.server 8899
# http://127.0.0.1:8899/
```

## Custom domain (jamesnightingale.net)

Not yet attached. The site currently serves from `https://jammy2211.github.io/`.

**Add the CNAME file BEFORE changing DNS.** GitHub Pages returns 404 for a domain it
has not been told about, so flipping DNS first blacks the site out until the CNAME
lands. Doing it in this order there is no downtime: the old host keeps serving the
domain until DNS moves, and the moment it moves GitHub is already configured.

1. Attach the domain (this repo):

   ```bash
   echo jamesnightingale.net > CNAME
   git add CNAME && git commit -m "Attach jamesnightingale.net" && git push
   ```

   From here `jammy2211.github.io` redirects to `jamesnightingale.net`, which still
   serves from the old host. That is expected.

2. At the DNS host (HostGator, nameservers `ns8509/ns8510.hostgator.com`), replace
   the single apex `A` record `50.116.114.85` with GitHub's four:

   ```
   A  @  185.199.108.153
   A  @  185.199.109.153
   A  @  185.199.110.153
   A  @  185.199.111.153
   ```

   Leave everything else alone. `www` is a CNAME to the apex and follows
   automatically; `mail`, `MX` and the SPF `TXT` record are separate and must not
   be touched or email breaks.

3. Wait for propagation — the record TTL is 14400s (4 hours). Check with
   `dig +short jamesnightingale.net A`.

4. GitHub then provisions a Let's Encrypt certificate, which needs DNS already
   pointing at it. Between the DNS flip and the certificate being issued, `https://`
   will warn. Do not enable enforcement until the cert exists:

   ```bash
   gh api repos/Jammy2211/Jammy2211.github.io/pages --jq .https_certificate.state
   # once "approved":
   gh api -X PUT repos/Jammy2211/Jammy2211.github.io/pages -f https_enforced=true
   ```

5. Verify every page on the real domain before touching the old host.

6. Cancel the old **hosting** plan. Keep the **domain registration** — they are
   separate line items, and GitHub Pages charges nothing for a custom domain.
   Check first whether any `@jamesnightingale.net` mailbox is in use: `MX` and
   `mail.jamesnightingale.net` both point at the old host, so cancelling hosting
   destroys that mail.

Registrar: Launchpad.com Inc. (Newfold/HostGator). Domain expires **2026-08-26**.
