import os

projects_data = [
    {
        "id": "p01",
        "title": "01 / FLOW — POMODORO & PRODUCTIVITY APP",
        "badge": "[EAS APP DOWNLOAD ⚡]",
        "copy1": "Productivity & Pomodoro session tracking app built with React Native for students, developers, and athletes.",
        "copy2": "Helps users stay focused, track performance metrics, and optimize daily study/work routines.",
        "meta": "REACT NATIVE · EXPO · REDUX · MOBILE APP · PRODUCTIVITY TRACKER"
    },
    {
        "id": "p02",
        "title": "02 / SIGNALIST — STOCK MARKET ANALYZER",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Real-time stock market analytics platform helping traders evaluate market trends, stock indicators & insights.",
        "copy2": "Combines financial domain algorithms with dynamic chart visualizations for actionable market intelligence.",
        "meta": "REACT · TYPESCRIPT · CHARTS · FINTECH · MARKET ANALYTICS"
    },
    {
        "id": "p03",
        "title": "03 / NAUMAN YASEEN MEDICAL CLINIC",
        "badge": "[LIVE SITE ↗]",
        "copy1": "Professional healthcare & medical clinic platform built in Next.js featuring SEO optimization & contact forms.",
        "copy2": "Showcases medical services, patient care information, and streamlined appointment inquiry workflows.",
        "meta": "NEXT.JS · TAILWIND CSS · SEO OPTIMIZED · HEALTHCARE · WEB PLATFORM"
    },
    {
        "id": "p04",
        "title": "04 / ZYRAH — E-COMMERCE STORE",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Feature-rich e-commerce web application with product catalog, cart, secure checkout, and order flow.",
        "copy2": "Scalable architecture with responsive UI serving customers across mobile and desktop devices.",
        "meta": "REACT · NODE.JS · MONGODB · REDUX · E-COMMERCE · PAYMENTS"
    },
    {
        "id": "p05",
        "title": "05 / METADATA — MECHANICAL KEYBOARD STORE",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Custom mechanical keyboard e-commerce store with interactive product displays and modern aesthetic UX.",
        "copy2": "Blends custom hardware specs with smooth web transitions for tech enthusiasts and gamers.",
        "meta": "NEXT.JS · TAILWIND CSS · THREE.JS · CUSTOM E-COMMERCE"
    },
    {
        "id": "p06",
        "title": "06 / ZENTRY KAPPA NINE — GAMING LANDING PAGE",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "High-performance gaming showcase platform featuring fluid web animations and immersive visual interactions.",
        "copy2": "Engineered with GSAP and Framer Motion for a state-of-the-art interactive gaming presentation.",
        "meta": "REACT · GSAP · FRAMER MOTION · GAMING UI · ANIMATIONS"
    },
    {
        "id": "p07",
        "title": "07 / MOJITO — BRAND LANDING PAGE",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Sleek beverage product landing page showcasing creative branding, interactive motion, and responsive layout.",
        "copy2": "Demonstrates modern frontend craftsmanship with smooth UI transitions and vibrant product styling.",
        "meta": "REACT · ANIME.JS · TAILWIND CSS · BRAND SHOWCASE"
    },
    {
        "id": "p08",
        "title": "08 / macOS DESKTOP STYLE PORTFOLIO",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Interactive macOS-inspired desktop operating system portfolio with draggable windows, dock & terminal.",
        "copy2": "Recreates authentic desktop UI components, app launcher, system controls, and window management.",
        "meta": "REACT · TYPESCRIPT · TAILWIND CSS · OS EMULATION · CREATIVE UI"
    },
    {
        "id": "p09",
        "title": "09 / ROYALE FRAGRANCES — LUXURY STORE",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Luxury fragrance e-commerce website with elegant product catalog, cart management, and premium branding.",
        "copy2": "Designed for high-end boutique retail with smooth navigation and mobile-first shopping experience.",
        "meta": "NEXT.JS · TAILWIND CSS · E-COMMERCE · LUXURY BRANDING"
    },
    {
        "id": "p10",
        "title": "10 / E-COMMERCE ADMIN DASHBOARD",
        "badge": "[LIVE DEMO ↗]",
        "copy1": "Comprehensive admin management suite with analytics, inventory controls, order tracking & user metrics.",
        "copy2": "Provides real-time business insights, data tables, and control workflows for store administrators.",
        "meta": "REACT · NODE.JS · EXPRESS · MONGODB · DASHBOARD & ANALYTICS"
    },
    {
        "id": "p11",
        "title": "11 / AI & MACHINE LEARNING PROJECT SUITE",
        "badge": "[PYTHON & TF 🧠]",
        "copy1": "House Price Prediction System (Regression) · Handwritten Digit Recognition (MNIST CNN Classifier).",
        "copy2": "Deep Neural Network architectures for pattern recognition, model evaluation, and predictive analytics.",
        "meta": "PYTHON · TENSORFLOW · DEEP LEARNING · SCIKIT-LEARN · NEURAL NETWORKS"
    }
]

def make_card_svg(p, is_dark):
    if is_dark:
        root_vars = "--ink:#FFFFFF; --copy:#EEEEEE; --meta:#CCCCCC; --rule:#555555; --paper:#000000; --link:#38bdf8;"
        light_vars = "--ink:#000000; --copy:#222222; --meta:#444444; --rule:#CCCCCC; --paper:#FFFFFF; --link:#0284c7;"
    else:
        root_vars = "--ink:#000000; --copy:#222222; --meta:#444444; --rule:#CCCCCC; --paper:#FFFFFF; --link:#0284c7;"
        light_vars = "--ink:#FFFFFF; --copy:#EEEEEE; --meta:#CCCCCC; --rule:#555555; --paper:#000000; --link:#38bdf8;"

    title = p['title'].replace("&", "&amp;")
    badge = p['badge'].replace("&", "&amp;")
    copy1 = p['copy1'].replace("&", "&amp;")
    copy2 = p['copy2'].replace("&", "&amp;")
    meta = p['meta'].replace("&", "&amp;")

    return f'''<svg viewBox="0 0 1000 110" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">
  <style>
    :root {{ {root_vars} }}
    @media (prefers-color-scheme: {"light" if is_dark else "dark"}) {{
      :root {{ {light_vars} }}
    }}
    .mono {{ font-family:ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,"Liberation Mono",monospace; }}
    .row {{ opacity:0; animation:reveal .55s cubic-bezier(.2,.7,.2,1) forwards; }}
    .rule {{ stroke:var(--rule); stroke-width:1.5; }}
    .title {{ fill:var(--ink); font-size:19px; font-weight:800; letter-spacing:0.5px; }}
    .copy {{ fill:var(--copy); font-size:14px; font-weight:500; }}
    .meta {{ fill:var(--meta); font-size:12.5px; font-weight:700; letter-spacing:.6px; }}
    .link-tag {{ fill:var(--link); font-size:13.5px; font-weight:800; letter-spacing:0.5px; }}
    @keyframes reveal {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @media (prefers-reduced-motion:reduce) {{ .row {{ animation:none; opacity:1; }} }}
  </style>

  <g class="mono row">
    <text class="title" x="48" y="24">{title} <tspan class="link-tag">{badge}</tspan></text>
    <text class="copy" x="48" y="49">{copy1}</text>
    <text class="copy" x="48" y="68">{copy2}</text>
    <text class="meta" x="48" y="87">{meta}</text>
    <line class="rule" x1="48" y1="104" x2="952" y2="104"/>
  </g>
</svg>
'''

os.makedirs('assets', exist_ok=True)
os.makedirs('assets/dark', exist_ok=True)

for p in projects_data:
    filename = f"{p['id']}.svg"
    with open(os.path.join('assets', filename), 'w', encoding='utf-8') as f:
        f.write(make_card_svg(p, False))
    with open(os.path.join('assets/dark', filename), 'w', encoding='utf-8') as f:
        f.write(make_card_svg(p, True))

print("Project card SVGs generated successfully!")
