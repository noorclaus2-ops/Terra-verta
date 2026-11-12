#!/usr/bin/env python3
"""Generates the Terra Verta site into ./public from the text below.

Run:  python3 build.py
All website text lives in TEXT (one block per language). The generated HTML
files are committed, so Cloudflare needs no build step.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent / "public"
SITE_NAME = "Terra Verta"

# ---------------------------------------------------------------------------
# Company details. Anything left as None is simply left off the site.
# ---------------------------------------------------------------------------
CONTACT_EMAIL = "Noor.Claus@UGent.be"
LINKEDIN_URL = None         # e.g. "https://www.linkedin.com/company/..."
ADDRESS_LINES = None        # e.g. ["Street 1", "1000 City", "Country"]
SITE_URL = None             # e.g. "https://www.terraverta.com" (no trailing slash)
# (name, role per language, photo); role None = no role shown, photo None = grey silhouette
TEAM = [("Noor Claus", {"en": "Founder", "nl": "Oprichter", "da": "Grundlægger"}, "/assets/team/noor-claus.jpg")]

LANGS = ["en", "nl", "da"]
ABOUT_SLUG = {"en": "about", "nl": "over-ons", "da": "om-os"}

TEXT = {
    "en": {
        "lang_name": "English",
        "nav_home": "Home", "nav_about": "About", "nav_contact": "Contact",
        "skip": "Skip to content",
        "title_home": "Terra Verta - AI-powered bioproduction of industrial biofertilizers",
        "desc": "Terra Verta combines artificial intelligence with industrial fermentation to produce biofertilizers at scale.",
        "hero": "AI-powered bioproduction of industrial biofertilizers",
        "vision_eyebrow": "Our vision",
        "vision_h": "We grow soil fertility with microorganisms",
        "vision_p": "Terra Verta produces biofertilizers: living microorganisms that help crops reach the nutrients they need. We combine artificial intelligence with industrial fermentation to make them reliably, at the scale agriculture requires.",
        "contact_us": "Contact us",
        "prod_eyebrow": "Our biofertilizers",
        "prod_h": "Biological fertility, built for industrial scale",
        "prod_p": "We design our products for industrial use: consistent quality from batch to batch, in volumes that fit large-scale agriculture.",
        "about_us": "About us",
        "plat_eyebrow": "Our platform",
        "plat_h": "Three steps from <em>microbe to field</em>",
        "steps": [
            ("AI-guided design", "Our AI models help select the microorganisms and growing conditions with the best chance of success, so we get there with fewer trials."),
            ("Precision fermentation", "We grow the microorganisms in controlled bioreactors, where every batch is measured and steered."),
            ("Industrial production", "We scale the process up to industrial volumes and formulate the result into a product that is ready to use."),
        ],
        "dash": {
            "eyebrow": "Inside the platform", "h": "Every batch, steered by data",
            "p": "Our software follows each fermentation live, predicts the outcome at industrial scale and suggests adjustments while the batch is still running.",
            "note": "Illustration with example data.",
            "elapsed": "Elapsed time", "elapsed_v": "18h 24m", "elapsed_s": "10h 36m remaining",
            "phase": "Current phase", "phase_s": "Phase 3 of 4",
            "scale": "Scale factor", "scale_s": "From 100 L pilot",
            "health": "Process health", "health_v": "Nominal", "health_s": "All parameters stable",
            "signals": "Live process signals", "do": "Dissolved oxygen", "target": "Target range",
            "ai": "AI prediction", "model": "Scale-up model",
            "yield": "Expected final yield", "risk": "Large-scale risk", "risk_v": "Low",
            "conf": "Confidence", "recs": "AI recommendations",
            "r1_tag": "High impact", "r1": "Increase aeration rate", "r1_e": "+2.8% yield",
            "r2_tag": "Stability", "r2": "Fine-tune feed rate", "r2_e": "Risk −4%",
            "vol": "2,000 L", "dec": ".",
        },
        "cta_h": "Want to know what biofertilizers can do for your business?",
        "cta_btn": "Get in touch",
        "f_contact": "Contact", "f_address": "Address",
        "ph_email": "[e-mail address]", "ph_address": "[company address]", "ph_linkedin": "[LinkedIn page]",
        "title_about": "About - Terra Verta",
        "about_h": "About",
        "about_tag": "A company building AI-powered bioproduction for industrial biofertilizers.",
        "mission_h": "Our mission",
        "mission_p": ["Fertilizers feed the crops that feed the world. We believe a growing share of them can be made by biology.",
                      "Terra Verta exists to make biofertilizers an industrial reality: produced at scale, with consistent quality."],
        "what_h": "What is a biofertilizer?",
        "what_p": ["A biofertilizer contains living microorganisms, such as bacteria or fungi. Applied to seed, plant or soil, they help the crop take up nutrients, for example by fixing nitrogen from the air or by releasing phosphorus that is locked in the soil."],
        "how_h": "How we work",
        "team_h": "Team",
        "ph_name": "[Name]", "ph_role": "[Role]",
        "nf_h": "This page does not exist.",
    },
    "nl": {
        "lang_name": "Nederlands",
        "nav_home": "Home", "nav_about": "Over ons", "nav_contact": "Contact",
        "skip": "Naar de inhoud",
        "title_home": "Terra Verta - AI-gestuurde bioproductie van industriële biomeststoffen",
        "desc": "Terra Verta combineert artificiële intelligentie met industriële fermentatie om biomeststoffen op grote schaal te produceren.",
        "hero": "AI-gestuurde bioproductie van industriële biomeststoffen",
        "vision_eyebrow": "Onze visie",
        "vision_h": "Wij kweken bodemvruchtbaarheid met micro-organismen",
        "vision_p": "Terra Verta produceert biomeststoffen: levende micro-organismen die gewassen helpen de voedingsstoffen op te nemen die ze nodig hebben. We combineren artificiële intelligentie met industriële fermentatie om ze betrouwbaar te maken, op de schaal die de landbouw vraagt.",
        "contact_us": "Contacteer ons",
        "prod_eyebrow": "Onze biomeststoffen",
        "prod_h": "Biologische vruchtbaarheid, gemaakt voor industriële schaal",
        "prod_p": "We ontwikkelen onze producten voor industrieel gebruik: een constante kwaliteit van batch tot batch, in volumes die passen bij grootschalige landbouw.",
        "about_us": "Over ons",
        "plat_eyebrow": "Ons platform",
        "plat_h": "In drie stappen van <em>microbe tot akker</em>",
        "steps": [
            ("AI-gestuurd ontwerp", "Onze AI-modellen helpen de micro-organismen en groeiomstandigheden te kiezen met de grootste kans op succes, zodat we met minder proeven ons doel bereiken."),
            ("Precisiefermentatie", "We kweken de micro-organismen in gecontroleerde bioreactoren, waar elke batch wordt gemeten en bijgestuurd."),
            ("Industriële productie", "We schalen het proces op naar industriële volumes en verwerken het resultaat tot een product dat klaar is voor gebruik."),
        ],
        "dash": {
            "eyebrow": "Een blik in het platform", "h": "Elke batch, gestuurd door data",
            "p": "Onze software volgt elke fermentatie live, voorspelt het resultaat op industriële schaal en stelt bijsturingen voor terwijl de batch nog loopt.",
            "note": "Illustratie met voorbeeldgegevens.",
            "elapsed": "Verstreken tijd", "elapsed_v": "18u 24m", "elapsed_s": "Nog 10u 36m",
            "phase": "Huidige fase", "phase_s": "Fase 3 van 4",
            "scale": "Schaalfactor", "scale_s": "Vanaf 100 L piloot",
            "health": "Procesgezondheid", "health_v": "Normaal", "health_s": "Alle parameters stabiel",
            "signals": "Live processignalen", "do": "Opgeloste zuurstof", "target": "Doelbereik",
            "ai": "AI-voorspelling", "model": "Opschalingsmodel",
            "yield": "Verwachte eindopbrengst", "risk": "Risico op grote schaal", "risk_v": "Laag",
            "conf": "Betrouwbaarheid", "recs": "AI-aanbevelingen",
            "r1_tag": "Grote impact", "r1": "Verhoog de beluchting", "r1_e": "+2,8% opbrengst",
            "r2_tag": "Stabiliteit", "r2": "Stel de voedingssnelheid bij", "r2_e": "Risico −4%",
            "vol": "2.000 L", "dec": ",",
        },
        "cta_h": "Benieuwd wat biomeststoffen voor uw bedrijf kunnen betekenen?",
        "cta_btn": "Neem contact op",
        "f_contact": "Contact", "f_address": "Adres",
        "ph_email": "[e-mailadres]", "ph_address": "[bedrijfsadres]", "ph_linkedin": "[LinkedIn-pagina]",
        "title_about": "Over ons - Terra Verta",
        "about_h": "Over ons",
        "about_tag": "Een bedrijf dat AI-gestuurde bioproductie bouwt voor industriële biomeststoffen.",
        "mission_h": "Onze missie",
        "mission_p": ["Meststoffen voeden de gewassen die de wereld voeden. Wij geloven dat een groeiend deel ervan door biologie gemaakt kan worden.",
                      "Terra Verta wil van biomeststoffen een industriële realiteit maken: geproduceerd op grote schaal, met een constante kwaliteit."],
        "what_h": "Wat is een biomeststof?",
        "what_p": ["Een biomeststof bevat levende micro-organismen, zoals bacteriën of schimmels. Aangebracht op zaad, plant of bodem helpen ze het gewas voedingsstoffen op te nemen, bijvoorbeeld door stikstof uit de lucht te binden of fosfor vrij te maken die in de bodem vastzit."],
        "how_h": "Hoe we werken",
        "team_h": "Team",
        "ph_name": "[Naam]", "ph_role": "[Functie]",
        "nf_h": "Deze pagina bestaat niet.",
    },
    "da": {
        "lang_name": "Dansk",
        "nav_home": "Forside", "nav_about": "Om os", "nav_contact": "Kontakt",
        "skip": "Gå til indhold",
        "title_home": "Terra Verta - AI-drevet bioproduktion af industriel biogødning",
        "desc": "Terra Verta kombinerer kunstig intelligens med industriel fermentering for at producere biogødning i stor skala.",
        "hero": "AI-drevet bioproduktion af industriel biogødning",
        "vision_eyebrow": "Vores vision",
        "vision_h": "Vi dyrker jordens frugtbarhed med mikroorganismer",
        "vision_p": "Terra Verta producerer biogødning: levende mikroorganismer, der hjælper afgrøder med at optage de næringsstoffer, de har brug for. Vi kombinerer kunstig intelligens med industriel fermentering for at fremstille dem pålideligt og i den skala, landbruget kræver.",
        "contact_us": "Kontakt os",
        "prod_eyebrow": "Vores biogødning",
        "prod_h": "Biologisk frugtbarhed, skabt til industriel skala",
        "prod_p": "Vi udvikler vores produkter til industriel brug: ensartet kvalitet fra batch til batch og i mængder, der passer til landbrug i stor skala.",
        "about_us": "Om os",
        "plat_eyebrow": "Vores platform",
        "plat_h": "Tre trin fra <em>mikrobe til mark</em>",
        "steps": [
            ("AI-styret design", "Vores AI-modeller hjælper med at vælge de mikroorganismer og vækstbetingelser, der har størst chance for succes, så vi når målet med færre forsøg."),
            ("Præcisionsfermentering", "Vi dyrker mikroorganismerne i kontrollerede bioreaktorer, hvor hver batch bliver målt og styret."),
            ("Industriel produktion", "Vi skalerer processen op til industrielle mængder og forarbejder resultatet til et produkt, der er klar til brug."),
        ],
        "dash": {
            "eyebrow": "Et kig ind i platformen", "h": "Hver batch, styret af data",
            "p": "Vores software følger hver fermentering live, forudsiger resultatet i industriel skala og foreslår justeringer, mens batchen stadig kører.",
            "note": "Illustration med eksempeldata.",
            "elapsed": "Forløbet tid", "elapsed_v": "18t 24m", "elapsed_s": "10t 36m tilbage",
            "phase": "Aktuel fase", "phase_s": "Fase 3 af 4",
            "scale": "Skaleringsfaktor", "scale_s": "Fra 100 L pilot",
            "health": "Processtatus", "health_v": "Normal", "health_s": "Alle parametre stabile",
            "signals": "Live processignaler", "do": "Opløst ilt", "target": "Målområde",
            "ai": "AI-forudsigelse", "model": "Opskaleringsmodel",
            "yield": "Forventet slutudbytte", "risk": "Risiko i stor skala", "risk_v": "Lav",
            "conf": "Sikkerhed", "recs": "AI-anbefalinger",
            "r1_tag": "Stor effekt", "r1": "Øg beluftningen", "r1_e": "+2,8 % udbytte",
            "r2_tag": "Stabilitet", "r2": "Finjustér tilførselshastigheden", "r2_e": "Risiko −4 %",
            "vol": "2.000 L", "dec": ",",
        },
        "cta_h": "Vil du vide, hvad biogødning kan gøre for din virksomhed?",
        "cta_btn": "Kontakt os",
        "f_contact": "Kontakt", "f_address": "Adresse",
        "ph_email": "[e-mailadresse]", "ph_address": "[virksomhedens adresse]", "ph_linkedin": "[LinkedIn-side]",
        "title_about": "Om os - Terra Verta",
        "about_h": "Om os",
        "about_tag": "En virksomhed, der bygger AI-drevet bioproduktion af industriel biogødning.",
        "mission_h": "Vores mission",
        "mission_p": ["Gødning giver næring til de afgrøder, der brødføder verden. Vi tror på, at en voksende del af den kan fremstilles biologisk.",
                      "Terra Verta vil gøre biogødning til en industriel realitet: produceret i stor skala og med ensartet kvalitet."],
        "what_h": "Hvad er biogødning?",
        "what_p": ["Biogødning indeholder levende mikroorganismer, for eksempel bakterier eller svampe. Når de tilføres frø, planter eller jord, hjælper de afgrøden med at optage næringsstoffer, blandt andet ved at binde kvælstof fra luften eller frigøre fosfor, der er bundet i jorden."],
        "how_h": "Sådan arbejder vi",
        "team_h": "Team",
        "ph_name": "[Navn]", "ph_role": "[Stilling]",
        "nf_h": "Denne side findes ikke.",
    },
}

# --------------------------------------------------------------------------- artwork
MARK = ('<svg viewBox="0 0 64 64" fill="currentColor" aria-hidden="true">'
        '<path d="M30 60V36h4v24z"/>'
        '<path d="M31 40C15 40 6 30 6 14c16 0 25 9 25 26z"/>'
        '<path d="M33 30c0-15 8-24 25-24 0 16-9 24-25 24z"/>'
        '</svg>')

ART_PLANT = '''<svg viewBox="0 0 800 800" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5aa7e0"/><stop offset="1" stop-color="#d8ecf7"/></linearGradient>
<linearGradient id="tank" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8fa3ad"/><stop offset=".45" stop-color="#e8eff2"/><stop offset="1" stop-color="#7d919b"/></linearGradient></defs>
<rect width="800" height="800" fill="url(#sky)"/>
<g fill="#fff" opacity=".75"><ellipse cx="170" cy="150" rx="120" ry="26"/><ellipse cx="260" cy="130" rx="90" ry="22"/><ellipse cx="610" cy="90" rx="110" ry="20"/></g>
<path d="M0 420C160 340 330 330 520 380s210 10 280-20v440H0z" fill="#4f9a45"/>
<path d="M0 470c190-70 380-40 560 0s180 10 240-10v340H0z" fill="#2f7a37"/>
<g stroke="#256a2e" stroke-width="3" opacity=".6"><path d="M0 520l800-60M0 560l800-50M0 600l800-40"/></g>
<g><rect x="60" y="430" width="120" height="370" rx="14" fill="url(#tank)"/><rect x="200" y="380" width="130" height="420" rx="14" fill="url(#tank)"/><rect x="350" y="450" width="110" height="350" rx="14" fill="url(#tank)"/>
<path d="M60 470h120M200 420h130M350 490h110" stroke="#6d818b" stroke-width="4"/>
<rect x="440" y="560" width="360" height="240" fill="#dfe7ea"/><path d="M440 560l180-60 180 60z" fill="#b9c6cc"/></g>
<g transform="translate(470 250) scale(4.2)" fill="#2fbf62"><path d="M30 60V36h4v24z"/><path d="M31 40C15 40 6 30 6 14c16 0 25 9 25 26z"/><path d="M33 30c0-15 8-24 25-24 0 16-9 24-25 24z"/></g>
</svg>'''

ART_FIELD = '''<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6e7b4"/><stop offset="1" stop-color="#fdf6dd"/></linearGradient></defs>
<rect width="800" height="600" fill="url(#dawn)"/>
<circle cx="610" cy="150" r="70" fill="#ffd34d"/>
<path d="M0 250c200-50 420-40 800 10v340H0z" fill="#6b4a2b"/>
<g fill="none" stroke="#2f9a45" stroke-width="16" stroke-linecap="round" stroke-dasharray="2 34">
<path d="M400 250L-260 600"/><path d="M400 250L-40 600"/><path d="M400 250L180 600"/><path d="M400 250L400 600"/><path d="M400 250L620 600"/><path d="M400 250L840 600"/><path d="M400 250L1060 600"/></g>
<g fill="none" stroke="#573a20" stroke-width="3" opacity=".5"><path d="M400 250L-150 600M400 250L70 600M400 250L290 600M400 250L510 600M400 250L730 600M400 250L950 600"/></g>
</svg>'''

PERSON = '<svg viewBox="0 0 64 64" fill="currentColor" aria-hidden="true"><circle cx="32" cy="22" r="12"/><path d="M8 60c0-14 10-22 24-22s24 8 24 22z"/></svg>'


# --------------------------------------------------------------------------- helpers
def home_path(lang):
    return f"/{lang}/"


def about_path(lang):
    return f"/{lang}/{ABOUT_SLUG[lang]}/"


def todo(text):
    return f'<span class="todo">{escape(text)}</span>'


def head(t, lang, title, paths):
    alts = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{(SITE_URL or "") + paths[l]}">' for l in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{(SITE_URL or "") + paths["en"]}">'
    canonical = f'<link rel="canonical" href="{SITE_URL + paths[lang]}">' if SITE_URL else ""
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(t["desc"])}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(t["desc"])}">
<meta property="og:type" content="website">
{canonical}{alts}
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/space-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
<script defer src="/assets/site.js"></script>
</head>
<body>
<a class="skip" href="#main">{escape(t["skip"])}</a>
'''


def header(t, lang, page, paths):
    cur = lambda p: ' aria-current="page"' if p == page else ""
    langs = "".join(
        f'<li><a href="{paths[l]}" lang="{l}" hreflang="{l}" title="{TEXT[l]["lang_name"]}"'
        f'{" aria-current=" + chr(34) + "true" + chr(34) if l == lang else ""}>{l.upper()}</a></li>'
        for l in LANGS
    )
    return f'''<header class="site-header"><div class="wrap">
<a class="brand" href="{home_path(lang)}">{MARK}<span>{SITE_NAME}</span></a>
<nav aria-label="{escape(t["nav_home"])}"><ul class="nav">
<li><a href="{home_path(lang)}"{cur("home")}>{escape(t["nav_home"])}</a></li>
<li><a href="{about_path(lang)}"{cur("about")}>{escape(t["nav_about"])}</a></li>
<li><a href="#contact">{escape(t["nav_contact"])}</a></li>
</ul></nav>
<ul class="langs" aria-label="Language">{langs}</ul>
</div></header>
'''


def footer(t):
    contact = []
    if CONTACT_EMAIL:
        contact.append(f'<a href="mailto:{escape(CONTACT_EMAIL)}">{escape(CONTACT_EMAIL)}</a>')
    if LINKEDIN_URL:
        contact.append(f'<a href="{escape(LINKEDIN_URL)}" rel="noopener">LinkedIn</a>')
    contact_col = (f'<div><h2>{escape(t["f_contact"])}</h2><p>{"<br>".join(contact)}</p></div>'
                   if contact else "")
    address_col = (f'<div><h2>{escape(t["f_address"])}</h2><address>'
                   + "<br>".join(escape(l) for l in ADDRESS_LINES) + "</address></div>"
                   if ADDRESS_LINES else "<div></div>")
    return f'''<footer class="site-footer" id="contact"><div class="wrap">
<div class="cols">
{contact_col}
{address_col}
<div class="big-mark">{MARK}</div>
</div>
<p class="legal"><span>© 2026 {SITE_NAME}</span></p>
</div></footer>
</body>
</html>
'''


def cta(t):
    return f'''<section class="cta reveal"><div class="wrap">
<h2>{escape(t["cta_h"])}</h2>
<a class="btn btn-solid" href="#contact">{escape(t["cta_btn"])}</a>
</div></section>
'''


def spark(values, color):
    """Small area chart as inline SVG."""
    w, h, lo, hi = 300, 70, min(values), max(values)
    span = (hi - lo) or 1
    pts = [(round(i * w / (len(values) - 1), 1), round(6 + (h - 12) * (1 - (v - lo) / span), 1))
           for i, v in enumerate(values)]
    line = " ".join(f"{x},{y}" for x, y in pts)
    return (f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true">'
            f'<polygon points="0,{h} {line} {w},{h}" fill="{color}" opacity=".14"/>'
            f'<polyline points="{line}" fill="none" stroke="{color}" stroke-width="2" vector-effect="non-scaling-stroke"/></svg>')


def dashboard(t):
    """Platform preview: an illustrative process dashboard with example data."""
    d = t["dash"]
    n = lambda x: x.replace(".", d["dec"])
    e = escape
    ph = [6.74, 6.72, 6.70, 6.69, 6.67, 6.66, 6.65, 6.66, 6.64, 6.65, 6.65, 6.66, 6.65, 6.66, 6.66, 6.65, 6.65]
    do = [58, 56, 52, 48, 43, 41, 39, 42, 40, 38, 41, 39, 41, 39, 40, 38, 40, 39]
    tile = lambda k, v, sub, cls="": (f'<div class="dash-tile"><span class="dash-label">{e(k)}</span>'
                                      f'<strong class="{cls}">{e(v)}</strong><small>{e(sub)}</small></div>')
    return f'''<section class="platform"><div class="wrap">
<div class="platform-intro reveal">
<p class="eyebrow">{e(d["eyebrow"])}</p>
<h2>{e(d["h"])}</h2>
<p>{e(d["p"])}</p>
</div>
<figure class="dash reveal">
<div class="dash-bar"><span class="dash-brand">{MARK}{SITE_NAME}</span>
<span class="dash-batch">TV-083 · <i>Azospirillum brasilense</i> · {e(d["vol"])}</span>
<span class="dash-live">Live</span></div>
<div class="dash-body">
<div class="dash-tiles">
{tile(d["elapsed"], d["elapsed_v"], d["elapsed_s"])}
{tile(d["phase"], "Fed-batch", d["phase_s"])}
{tile(d["scale"], "20×", d["scale_s"])}
{tile(d["health"], d["health_v"], d["health_s"], "ok")}
</div>
<div class="dash-grid">
<div class="dash-card">
<h3>{e(d["signals"])}</h3>
<div class="dash-signals">
<div class="dash-signal"><span class="dash-label">pH</span><strong>{n("6.65")}</strong>{spark(ph, "#2f7fd6")}
<small>{e(d["target"])} <b>{n("6.50")} – {n("6.80")}</b></small></div>
<div class="dash-signal"><span class="dash-label">{e(d["do"])}</span><strong>{n("42.1")} <em>% sat.</em></strong>{spark(do, "#1f9d4d")}
<small>{e(d["target"])} <b>35 – 50%</b></small></div>
</div>
</div>
<div class="dash-card dash-ai">
<div class="dash-ai-head"><h3>{e(d["ai"])}</h3><span>{e(d["model"])}</span></div>
<span class="dash-label">{e(d["yield"])}</span>
<strong class="dash-big">{n("4.2")} × 10<sup>9</sup> <em>CFU/ml</em></strong>
<div class="dash-pair">
<div><span class="dash-label">{e(d["risk"])}</span><strong class="ok">{e(d["risk_v"])}</strong></div>
<div><span class="dash-label">{e(d["conf"])}</span><strong>94%</strong></div>
</div>
<div class="dash-meter"><i style="width:94%"></i></div>
</div>
</div>
<div class="dash-card">
<h3>{e(d["recs"])}</h3>
<div class="dash-recs">
<div class="dash-rec"><span class="dash-tag">{e(d["r1_tag"])}</span><b>{e(d["r1"])}</b><small>{e(d["r1_e"])}</small></div>
<div class="dash-rec"><span class="dash-tag alt">{e(d["r2_tag"])}</span><b>{e(d["r2"])}</b><small>{e(d["r2_e"])}</small></div>
</div>
</div>
</div>
<figcaption>{e(d["note"])}</figcaption>
</figure>
</div></section>
'''


def home(lang):
    t = TEXT[lang]
    paths = {l: home_path(l) for l in LANGS}
    tabs = "".join(
        f'<li><button type="button" role="tab" aria-selected="false">{escape(h)}</button></li>'
        for h, _ in t["steps"])
    panels = "".join(
        f'<div class="pillar-panel"><span class="num">{i}</span><div><h3>{escape(h)}</h3><p>{escape(p)}</p></div></div>'
        for i, (h, p) in enumerate(t["steps"], 1))
    return head(t, lang, t["title_home"], paths) + header(t, lang, "home", paths) + f'''<main id="main">
<section class="hero">
<div class="hero-art" aria-hidden="true"><i class="o1"></i><i class="o4"></i><i class="o2"></i><i class="o3"></i></div>
<div><div class="hero-mark">{MARK}</div><h1>{escape(t["hero"])}</h1></div>
</section>

<section class="split">
<div class="art">{ART_PLANT}</div>
<div class="text reveal">
<p class="eyebrow">{escape(t["vision_eyebrow"])}</p>
<h2>{escape(t["vision_h"])}</h2>
<p>{escape(t["vision_p"])}</p>
<div class="btn-row"><a class="btn" href="#contact">{escape(t["contact_us"])}</a></div>
</div>
</section>

<section class="split flip">
<div class="art">{ART_FIELD}</div>
<div class="text reveal">
<p class="eyebrow">{escape(t["prod_eyebrow"])}</p>
<h2>{escape(t["prod_h"])}</h2>
<p>{escape(t["prod_p"])}</p>
<div class="btn-row"><a class="btn" href="{about_path(lang)}">{escape(t["about_us"])}</a><a class="btn" href="#contact">{escape(t["contact_us"])}</a></div>
</div>
</section>

<section class="pillars" data-pillars><div class="wrap">
<div class="pillar-panels" aria-live="polite">{panels}</div>
<div class="reveal">
<p class="eyebrow">{escape(t["plat_eyebrow"])}</p>
<h2>{t["plat_h"]}</h2>
<ul class="pillar-tabs" role="tablist">{tabs}</ul>
</div>
</div></section>

{dashboard(t)}
{cta(t)}</main>
''' + footer(t)


def about(lang):
    t = TEXT[lang]
    paths = {l: about_path(l) for l in LANGS}
    paras = lambda ps: "".join(f"<p>{escape(p)}</p>" for p in ps)
    steps = "".join(
        f'<li><span class="num">{i}</span><h3>{escape(h)}</h3><p>{escape(p)}</p></li>'
        for i, (h, p) in enumerate(t["steps"], 1))
    team = "".join(
        '<div class="member"><div class="photo">'
        + (f'<img src="{escape(ph)}" alt="{escape(n)}" width="640" height="640" loading="lazy">' if ph else PERSON)
        + f'</div><h3>{escape(n)}</h3>{"<p>" + escape(r[lang]) + "</p>" if r else ""}</div>'
        for n, r, ph in TEAM)
    team_section = f'''<section class="prose reveal"><div class="wrap">
<h2>{escape(t["team_h"])}</h2><div class="team">{team}</div>
</div></section>
''' if TEAM else ""
    return head(t, lang, t["title_about"], paths) + header(t, lang, "about", paths) + f'''<main id="main">
<section class="page-head"><div class="wrap">
<h1>{escape(t["about_h"])}</h1>
<p>{escape(t["about_tag"])}</p>
</div></section>

<section class="prose reveal"><div class="wrap">
<h2>{escape(t["mission_h"])}</h2><div>{paras(t["mission_p"])}</div>
</div></section>

<section class="prose reveal"><div class="wrap">
<h2>{escape(t["what_h"])}</h2><div>{paras(t["what_p"])}</div>
</div></section>

<section class="prose reveal"><div class="wrap">
<h2>{escape(t["how_h"])}</h2><ol class="steps">{steps}</ol>
</div></section>

{team_section}
{cta(t)}</main>
''' + footer(t)


def root_index():
    links = "".join(f'<li><a class="btn" href="/{l}/" lang="{l}">{TEXT[l]["lang_name"]}</a></li>' for l in LANGS)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE_NAME}</title>
<meta name="description" content="{escape(TEXT["en"]["desc"])}">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<script>
(function () {{
  var supported = {LANGS!r}, pick = "en";
  var prefs = navigator.languages || [navigator.language || "en"];
  for (var i = 0; i < prefs.length; i++) {{
    var code = String(prefs[i]).toLowerCase().split("-")[0];
    if (supported.indexOf(code) !== -1) {{ pick = code; break; }}
  }}
  location.replace("/" + pick + "/");
}})();
</script>
<noscript><meta http-equiv="refresh" content="0; url=/en/"></noscript>
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<main class="center-page"><div><h1>{SITE_NAME}</h1><ul>{links}</ul></div></main>
</body>
</html>
'''


def not_found():
    lines = "".join(f'<p lang="{l}">{escape(TEXT[l]["nf_h"])}</p>' for l in LANGS)
    links = "".join(f'<li><a class="btn" href="/{l}/" lang="{l}">{TEXT[l]["lang_name"]}</a></li>' for l in LANGS)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 - {SITE_NAME}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<main class="center-page"><div><h1>404</h1>{lines}<br><ul>{links}</ul></div></main>
</body>
</html>
'''


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT.parent))


if __name__ == "__main__":
    write("index.html", root_index())
    write("404.html", not_found())
    write("assets/logo.svg", MARK.replace('fill="currentColor"', 'xmlns="http://www.w3.org/2000/svg" fill="#1f9d4d"'))
    for lang in LANGS:
        write(f"{lang}/index.html", home(lang))
        write(f"{lang}/{ABOUT_SLUG[lang]}/index.html", about(lang))
