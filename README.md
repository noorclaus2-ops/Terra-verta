# Terra Verta website

Static website in English, Dutch and Danish. Cloudflare publishes the `public/` folder
automatically on every push to `main`.

## Changing text

All text is in `build.py`, in the `TEXT` block (one section per language). Company details
(e-mail, LinkedIn, address, team, site address) are at the top of the same file; anything
left as `None` is left off the site.

After editing, regenerate the pages and commit:

```bash
python3 build.py
```

## Layout

```
build.py          text + page templates, writes public/
wrangler.jsonc    Cloudflare configuration
public/           the published site
  assets/         style.css, site.js, logo, fonts
  en/ nl/ da/     home and about page per language
```

## Preview locally

```bash
python3 -m http.server 8000 --directory public
```

## Credits

Typeface: Space Grotesk (SIL Open Font License, see `public/assets/fonts/`).
