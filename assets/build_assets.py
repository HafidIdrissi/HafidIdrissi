#!/usr/bin/env python3
"""Generate the self-hosted SVG components for the profile README.

GitHub allows no CSS in a README, so the only way to control typography and
layout is to draw it. These render once here and are committed, in a dark and a
light variant each, served through <picture> so they follow the reader's theme.

Four rules govern these files:

1. Nothing animated. Verified on the live profile: GitHub serves README SVGs
   through its image proxy and does not run the CSS animation inside them. An
   animated SVG freezes on its first frame, and anything starting at opacity 0
   never appears at all. Everything here is static.
2. Nothing that changes. A release number or test status baked into an SVG goes
   stale silently; those stay live shields.io badges in the Markdown.
3. Nothing unverified. The data flow is drawn from Time Tracker's actual
   architecture: a local SQLite file and an HTML report, with no network egress.
4. Nothing load-bearing. A 1200-unit asset shrinks to 0.3x on a phone, so no
   fact may live only in an image. Every claim drawn here is also written in the
   Markdown around it.

Sizing follows a 1200-unit viewBox rendered at roughly 900 CSS pixels: essential
text at 20+ units, supporting labels at 18+, titles at 40+. Web fonts do not
load through the image proxy, so everything uses system font stacks.

Usage: python assets/build_assets.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent
W = 1200

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"

THEMES = {
    "dark": {
        "bg": "#0A0B0D", "panel": "#12151B", "inner": "#171B23", "line": "#232833",
        "text": "#E9EBEF", "muted": "#98A1B0", "faint": "#6A7484",
        "accent": "#FF6A3D", "accent2": "#6366F1", "ok": "#3DDC97", "glow": 0.20,
    },
    "light": {
        "bg": "#FBFBFA", "panel": "#FFFFFF", "inner": "#F4F4F2", "line": "#E2E2DD",
        "text": "#16181D", "muted": "#5C6470", "faint": "#89909C",
        "accent": "#D94F1E", "accent2": "#4F46E5", "ok": "#0F9D6B", "glow": 0.13,
    },
}


def hero(t):
    """Thesis-led banner. The position comes first, the job title second."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 300" width="{W}" height="300" role="img" aria-labelledby="heroTitle heroDesc">
  <title id="heroTitle">Hafid Idrissi &#8212; software engineer</title>
  <desc id="heroDesc">I build software that doesn&#8217;t phone home. Local-first tools people can audit, and the cloud and embedded work behind them. Azure, Kubernetes, Python, TypeScript, ROS, PyMC.</desc>
  <defs>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['accent']}"/><stop offset="100%" stop-color="{t['accent2']}"/>
    </linearGradient>
    <radialGradient id="gA" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="{t['accent']}" stop-opacity="{t['glow']}"/>
      <stop offset="100%" stop-color="{t['accent']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="gB" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="{t['accent2']}" stop-opacity="{t['glow']}"/>
      <stop offset="100%" stop-color="{t['accent2']}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="frame"><rect width="{W}" height="300" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="{W}" height="300" fill="{t['bg']}"/>
    <ellipse cx="1055" cy="34" rx="330" ry="215" fill="url(#gA)"/>
    <ellipse cx="1200" cy="285" rx="285" ry="185" fill="url(#gB)"/>
    <rect width="{W}" height="300" fill="none" stroke="{t['line']}" stroke-width="2" rx="18"/>
  </g>

  <text x="72" y="70" font-family="{MONO}" font-size="17" letter-spacing="3.4" fill="{t['faint']}">HAFID IDRISSI &#183; SOFTWARE ENGINEER</text>
  <text x="72" y="142" font-family="{SANS}" font-size="46" font-weight="700" letter-spacing="-1.4" fill="{t['text']}">I build software that doesn&#8217;t phone home.</text>
  <rect x="73" y="166" width="70" height="4" rx="2" fill="url(#rule)"/>
  <text x="72" y="212" font-family="{SANS}" font-size="21" fill="{t['muted']}">Local-first tools people can actually audit &#8212; and the cloud and</text>
  <text x="72" y="242" font-family="{SANS}" font-size="21" fill="{t['muted']}">embedded work behind them.</text>
  <text x="72" y="276" font-family="{MONO}" font-size="18" fill="{t['faint']}">Azure &#183; Kubernetes &#183; Python &#183; TypeScript &#183; ROS &#183; PyMC</text>
</svg>
'''


def tracker_card(t):
    """The signature visual: Time Tracker's data flow, and where it stops."""
    boxes = [
        (76, "Your activity", "app, window, tab, idle"),
        (450, "timetracker.db", "local SQLite file"),
        (824, "report.html", "opens offline"),
    ]
    bw = 300
    cells = ""
    for x, title, sub in boxes:
        cells += f'''
  <rect x="{x}" y="176" width="{bw}" height="92" rx="12" fill="{t['inner']}" stroke="{t['line']}"/>
  <text x="{x + 24}" y="216" font-family="{MONO}" font-size="20" font-weight="600" fill="{t['text']}">{title}</text>
  <text x="{x + 24}" y="245" font-family="{SANS}" font-size="18" fill="{t['faint']}">{sub}</text>'''

    arrows = ""
    for ax in (392, 766):
        arrows += f'''
  <line x1="{ax}" y1="222" x2="{ax + 40}" y2="222" stroke="{t['accent']}" stroke-width="2.4"/>
  <path d="M{ax + 40} 222 l-10 -6 v12 z" fill="{t['accent']}"/>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 396" width="{W}" height="396" role="img" aria-labelledby="ttTitle ttDesc">
  <title id="ttTitle">Time Tracker &#8212; where your activity data goes</title>
  <desc id="ttDesc">On your machine: your activity (app, window, tab, idle) is written to timetracker.db, a local SQLite file, and rendered to report.html, which opens offline. Nothing crosses that boundary: no account, no server, no telemetry.</desc>
  <defs>
    <linearGradient id="edge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{t['accent']}"/><stop offset="100%" stop-color="{t['accent2']}"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="{W - 2}" height="394" rx="18" fill="{t['panel']}" stroke="{t['line']}" stroke-width="2"/>
  <rect x="1" y="1" width="6" height="394" fill="url(#edge)"/>

  <circle cx="48" cy="56" r="8" fill="{t['accent']}"/>
  <text x="70" y="65" font-family="{SANS}" font-size="28" font-weight="700" letter-spacing="-0.6" fill="{t['text']}">Time Tracker</text>
  <rect x="262" y="40" width="132" height="30" rx="15" fill="none" stroke="{t['ok']}" stroke-width="1.6"/>
  <text x="328" y="61" text-anchor="middle" font-family="{MONO}" font-size="15" letter-spacing="1.2" fill="{t['ok']}">OPEN SOURCE</text>
  <text x="{W - 44}" y="64" text-anchor="end" font-family="{MONO}" font-size="18" fill="{t['faint']}">Windows 10 &#183; 11</text>

  <text x="44" y="112" font-family="{SANS}" font-size="21" fill="{t['muted']}">Where your activity data goes &#8212; the whole diagram.</text>

  <rect x="44" y="136" width="{W - 88}" height="164" rx="14" fill="none" stroke="{t['line']}" stroke-dasharray="7 5"/>
  <text x="64" y="164" font-family="{MONO}" font-size="15" letter-spacing="2.4" fill="{t['faint']}">YOUR MACHINE</text>
{cells}{arrows}

  <circle cx="56" cy="345" r="12" fill="none" stroke="{t['accent']}" stroke-width="2.2"/>
  <path d="M50 339 l12 12 M62 339 l-12 12" stroke="{t['accent']}" stroke-width="2.2" stroke-linecap="round"/>
  <text x="82" y="341" font-family="{SANS}" font-size="20" font-weight="600" fill="{t['text']}">Nothing crosses that boundary.</text>
  <text x="82" y="366" font-family="{SANS}" font-size="18" fill="{t['faint']}">No account, no server, no telemetry &#8212; so there is nothing to opt out of.</text>
</svg>
'''


def main():
    for name, fn in (("hero", hero), ("time-tracker-card", tracker_card)):
        for theme, tokens in THEMES.items():
            (OUT / f"{name}-{theme}.svg").write_text(fn(tokens), encoding="utf-8")
    print("written: hero-{dark,light}.svg, time-tracker-card-{dark,light}.svg")
    print("all static — GitHub does not run animation inside README SVGs")


if __name__ == "__main__":
    main()
