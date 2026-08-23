#!/usr/bin/env python3
"""Render the animated GIFs for the profile README.

Verified on the live profile: GitHub does not run CSS animation inside a README
SVG — an animated SVG freezes on its first frame. GIF does play. So motion here
is rasterised: each frame is a parameterised SVG, rendered by headless Chrome,
then assembled by ffmpeg with a per-clip palette.

Every GIF has a static SVG counterpart from build_assets.py, and every fact it
shows is also written in the Markdown. Motion is decoration; if a reader has
GIFs disabled, or reads on a phone where the type is too small, nothing is lost.

Usage:
    python assets/build_motion.py            # both clips
    python assets/build_motion.py dataflow   # one clip
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

OUT = Path(__file__).resolve().parent
W = 1200

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"

THEMES = {
    "dark": {
        "bg": "#0A0B0D", "panel": "#12151B", "inner": "#171B23", "line": "#232833",
        "text": "#E9EBEF", "muted": "#98A1B0", "faint": "#6A7484",
        "accent": "#FF6A3D", "accent2": "#6366F1", "ok": "#3DDC97",
    },
    "light": {
        "bg": "#FBFBFA", "panel": "#FFFFFF", "inner": "#F4F4F2", "line": "#E2E2DD",
        "text": "#16181D", "muted": "#5C6470", "faint": "#89909C",
        "accent": "#D94F1E", "accent2": "#4F46E5", "ok": "#0F9D6B",
    },
}
T = THEMES["dark"]   # rebound per render

CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "google-chrome", "chromium",
]


def find_chrome():
    for c in CHROME:
        if Path(c).exists():
            return c
        f = shutil.which(c)
        if f:
            return f
    raise SystemExit("No Chrome binary found for frame rendering.")


def ease(x):
    """Smootherstep, so packets accelerate and settle rather than sliding linearly."""
    x = max(0.0, min(1.0, x))
    return x * x * x * (x * (x * 6 - 15) + 10)


def _dot(cx, cy, T, vertical=False):
    """A travelling packet with a short motion trail behind it."""
    tail = (f'<rect x="{cx - 4:.1f}" y="{cy - 26:.1f}" width="8" height="26" rx="4" '
            f'fill="{T["accent"]}" opacity="0.28"/>' if vertical else
            f'<rect x="{cx - 30:.1f}" y="{cy - 4:.1f}" width="30" height="8" rx="4" '
            f'fill="{T["accent"]}" opacity="0.28"/>')
    return (tail + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="10" fill="{T["accent"]}"/>'
                   f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="16" fill="none" '
                   f'stroke="{T["accent"]}" stroke-width="1.6" opacity="0.35"/>')


# ────────────────────────────── data flow clip ──────────────────────────────

BOXES = [(76, "Your activity", "app, window, tab, idle"),
         (450, "timetracker.db", "local SQLite file"),
         (824, "report.html", "opens offline")]
BW = 300


def dataflow_frame(t, T):
    """One frame of the data path. t in [0,1).

    Beat 1 (0.00-0.34): a packet leaves the activity box for the database.
    Beat 2 (0.34-0.62): it moves on to the report.
    Beat 3 (0.62-1.00): a packet tries to leave the machine and is stopped.
    """
    cells = ""
    for i, (x, title, sub) in enumerate(BOXES):
        lit = (i == 0 and t < 0.12) or (0.30 < t < 0.44 and i == 1) or (0.58 < t < 0.72 and i == 2)
        stroke = T["accent"] if lit else T["line"]
        sw = 2.2 if lit else 1
        cells += f'''
  <rect x="{x}" y="176" width="{BW}" height="92" rx="12" fill="{T['inner']}" stroke="{stroke}" stroke-width="{sw}"/>
  <text x="{x + 24}" y="216" font-family="{MONO}" font-size="20" font-weight="600" fill="{T['text']}">{title}</text>
  <text x="{x + 24}" y="245" font-family="{SANS}" font-size="18" fill="{T['faint']}">{sub}</text>'''

    arrows = ""
    for ax in (392, 766):
        arrows += f'''
  <line x1="{ax}" y1="222" x2="{ax + 40}" y2="222" stroke="{T['accent']}" stroke-width="2.4" opacity="0.5"/>
  <path d="M{ax + 40} 222 l-10 -6 v12 z" fill="{T['accent']}" opacity="0.5"/>'''

    packet = ""
    if t < 0.34:                                   # activity → database
        p = ease(t / 0.34)
        packet = _dot(376 + p * 74, 222, T)
    elif t < 0.62:                                 # database → report
        p = ease((t - 0.34) / 0.28)
        packet = _dot(750 + p * 74, 222, T)
    else:                                          # the escape attempt, refused
        p = (t - 0.62) / 0.38
        if p < 0.45:
            y = 268 + ease(p / 0.45) * 44
            packet = _dot(600, y, T, vertical=True)
        elif p < 0.72:                             # blocked at the boundary
            k = (p - 0.45) / 0.27
            r = 11 + k * 22
            packet = (f'<circle cx="600" cy="312" r="{r:.1f}" fill="none" '
                      f'stroke="{T["accent"]}" stroke-width="{2.4 * (1 - k):.2f}" opacity="{1 - k:.2f}"/>')

    # the refusal bar pulses only while something is pushing against it
    hot = 0.62 < t < 0.92
    bar = T["accent"] if hot else T["line"]
    barw = 3 if hot else 1.6

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 396" width="{W}" height="396">
  <rect x="1" y="1" width="{W - 2}" height="394" rx="18" fill="{T['panel']}" stroke="{T['line']}" stroke-width="2"/>
  <rect x="1" y="1" width="6" height="394" fill="{T['accent']}"/>

  <circle cx="48" cy="56" r="8" fill="{T['accent']}"/>
  <text x="70" y="65" font-family="{SANS}" font-size="28" font-weight="700" fill="{T['text']}">Time Tracker</text>
  <rect x="262" y="40" width="132" height="30" rx="15" fill="none" stroke="{T['ok']}" stroke-width="1.6"/>
  <text x="328" y="61" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{T['ok']}">OPEN SOURCE</text>
  <text x="{W - 44}" y="64" text-anchor="end" font-family="{MONO}" font-size="18" fill="{T['faint']}">Windows 10 &#183; 11</text>

  <text x="44" y="112" font-family="{SANS}" font-size="21" fill="{T['muted']}">Where your activity data goes &#8212; the whole diagram.</text>

  <rect x="44" y="136" width="{W - 88}" height="176" rx="14" fill="none" stroke="{bar}" stroke-width="{barw}" stroke-dasharray="7 5"/>
  <text x="64" y="164" font-family="{MONO}" font-size="15" fill="{T['faint']}">YOUR MACHINE</text>
{cells}{arrows}
  {packet}

  <circle cx="56" cy="352" r="12" fill="none" stroke="{T['accent']}" stroke-width="2.2"/>
  <path d="M50 346 l12 12 M62 346 l-12 12" stroke="{T['accent']}" stroke-width="2.2" stroke-linecap="round"/>
  <text x="82" y="348" font-family="{SANS}" font-size="20" font-weight="600" fill="{T['text']}">Nothing crosses that boundary.</text>
  <text x="82" y="373" font-family="{SANS}" font-size="18" fill="{T['faint']}">No account, no server, no telemetry.</text>
</svg>
'''


# ──────────────────────────────── hero clip ────────────────────────────────

THESIS = "I build software that doesn\u2019t phone home."


def hero_frame(t, T):
    """Types the thesis, holds it, then rests. t in [0,1)."""
    type_end = 0.55
    if t < type_end:
        n = int(len(THESIS) * (t / type_end))
        shown, cursor = THESIS[:n], True
    else:
        shown, cursor = THESIS, (int(t * 14) % 2 == 0)

    esc = shown.replace("&", "&amp;").replace("<", "&lt;")
    cx = 72 + len(shown) * 24.4
    car = (f'<rect x="{cx:.0f}" y="112" width="16" height="38" fill="{T["accent"]}"/>'
           if cursor else "")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 300" width="{W}" height="300">
  <defs>
    <linearGradient id="r" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{T['accent']}"/><stop offset="100%" stop-color="{T['accent2']}"/>
    </linearGradient>
    <clipPath id="f"><rect width="{W}" height="300" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#f)">
    <rect width="{W}" height="300" fill="{T['bg']}"/>
    <rect width="{W}" height="300" fill="none" stroke="{T['line']}" stroke-width="2" rx="18"/>
  </g>
  <text x="72" y="70" font-family="{MONO}" font-size="17" letter-spacing="3.4" fill="{T['faint']}">HAFID IDRISSI &#183; SOFTWARE ENGINEER</text>
  <text x="72" y="142" font-family="{SANS}" font-size="46" font-weight="700" letter-spacing="-1.4" fill="{T['text']}">{esc}</text>
  {car}
  <rect x="73" y="166" width="70" height="4" rx="2" fill="url(#r)"/>
  <text x="72" y="212" font-family="{SANS}" font-size="21" fill="{T['muted']}">Local-first tools people can actually audit &#8212; and the cloud and</text>
  <text x="72" y="242" font-family="{SANS}" font-size="21" fill="{T['muted']}">embedded work behind them.</text>
  <text x="72" y="276" font-family="{MONO}" font-size="18" fill="{T['faint']}">Azure &#183; Kubernetes &#183; Python &#183; TypeScript &#183; ROS &#183; PyMC</text>
</svg>
'''


# ──────────────────────────────── pipeline ────────────────────────────────

def render(name, frame_fn, n_frames, size, fps, theme):
    chrome = find_chrome()
    w, h = size
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for i in range(n_frames):
            svg = tmp / f"f{i:03d}.svg"
            svg.write_text(frame_fn(i / n_frames, THEMES[theme]), encoding="utf-8")
            subprocess.run(
                [chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
                 "--hide-scrollbars", "--force-device-scale-factor=1",
                 f"--user-data-dir={tmp}/p{i}",
                 f"--window-size={w},{h}",
                 f"--screenshot={tmp / f'f{i:03d}.png'}", svg.as_uri()],
                check=True, capture_output=True, timeout=90)

        out = OUT / f"{name}-{theme}.gif"
        pal = tmp / "pal.png"
        common = ["-framerate", str(fps), "-i", str(tmp / "f%03d.png")]
        subprocess.run(["ffmpeg", "-y", *common, "-vf",
                        "palettegen=max_colors=64:stats_mode=diff", str(pal)],
                       check=True, capture_output=True)
        subprocess.run(["ffmpeg", "-y", *common, "-i", str(pal), "-lavfi",
                        "paletteuse=dither=bayer:bayer_scale=3", "-loop", "0", str(out)],
                       check=True, capture_output=True)
        return out


CLIPS = {
    "dataflow": (dataflow_frame, 40, (W, 396), 14),
    "hero":     (hero_frame,     44, (W, 300), 16),
}


def main():
    for name in (sys.argv[1:] or CLIPS):
        fn, n, size, fps = CLIPS[name]
        for theme in THEMES:
            out = render(f"{name}-motion", fn, n, size, fps, theme)
            print(f"  {out.name}: {n} frames @ {fps}fps, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
