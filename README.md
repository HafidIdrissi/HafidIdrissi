<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/main/assets/hero-motion-dark.gif" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/main/assets/hero-motion-light.gif" />
  <img src="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/main/assets/hero-motion-dark.gif" alt="Hafid Idrissi, software engineer. I build software that doesn't phone home — local-first tools people can actually audit, and the cloud and embedded work behind them. Azure, Kubernetes, Python, TypeScript, ROS, PyMC." width="900" />
</picture>

### I build software that doesn't phone home.

[![Portfolio](https://img.shields.io/badge/Portfolio-hidrissi.tech-F97316?style=for-the-badge&logo=googlechrome&logoColor=white)](https://hidrissi.tech)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hafid-idrissi/)
[![Contact](https://img.shields.io/badge/Contact-6366F1?style=for-the-badge&logo=gmail&logoColor=white)](mailto:idrissihafez@gmail.com)

**Time Tracker** sends nothing &nbsp;·&nbsp; **GoEditPDF** keeps your files in the browser &nbsp;·&nbsp; private **AKS** networking at Hager &nbsp;·&nbsp; **LiDAR SLAM** at Mirion

</div>

## Featured open-source project

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/main/assets/dataflow-motion-dark.gif" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/main/assets/dataflow-motion-light.gif" />
  <img src="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/main/assets/dataflow-motion-dark.gif" alt="Animated diagram: your activity flows into timetracker.db, a local SQLite file, then into report.html which opens offline. A final packet tries to leave your machine and is stopped at the boundary — no account, no server, no telemetry." width="900" />
</picture>

Most time trackers answer "where did my time go?" by uploading your activity to somebody's server.
This one answers it without the upload — the diagram above is the entire data path, written out:

**your activity** (app, window, tab, idle) → **`timetracker.db`** (a local SQLite file you own) →
**`report.html`** (opens offline). No account, no server, no telemetry, so there is nothing to opt out of.

[![Latest release](https://img.shields.io/github/v/release/HafidIdrissi/Time-Tracker?display_name=tag&sort=semver&color=F97316&label=latest%20release)](https://github.com/HafidIdrissi/Time-Tracker/releases/latest)
[![Tests](https://img.shields.io/github/actions/workflow/status/HafidIdrissi/Time-Tracker/tests.yml?branch=main&label=tests)](https://github.com/HafidIdrissi/Time-Tracker/actions/workflows/tests.yml)
[![License](https://img.shields.io/github/license/HafidIdrissi/Time-Tracker?color=6366F1)](https://github.com/HafidIdrissi/Time-Tracker/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://github.com/HafidIdrissi/Time-Tracker)
[![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4?logo=windows&logoColor=white)](https://github.com/HafidIdrissi/Time-Tracker/releases/latest)
[![Stars](https://img.shields.io/github/stars/HafidIdrissi/Time-Tracker?color=F97316)](https://github.com/HafidIdrissi/Time-Tracker)

<div align="center">
<a href="https://github.com/HafidIdrissi/Time-Tracker">
<img src="https://raw.githubusercontent.com/HafidIdrissi/Time-Tracker/main/assets/report-preview.svg" alt="Local Time Tracker activity report showing active time, idle time, totals by category, a timeline and the applications used" width="760" />
</a>
</div>

**Beyond the diagram**

- **No manual timers** — it tracks the foreground application, window title, browser tab and idle periods on its own
- **Reports worth reading** — daily and seven-day summaries, charts, categories and per-application totals
- **Python, `pywin32` and `psutil`**, with a test suite that runs in CI on every push
- **Windows installer** on every release with a published SHA-256 checksum — and [not code-signed](https://github.com/HafidIdrissi/Time-Tracker/blob/main/SIGNING.md), which the repository states plainly rather than hiding

<div align="center">

[![Download latest release](https://img.shields.io/badge/Download%20latest%20release-F97316?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/HafidIdrissi/Time-Tracker/releases/latest)
[![View source code](https://img.shields.io/badge/View%20source%20code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HafidIdrissi/Time-Tracker)

[![Contribute](https://img.shields.io/badge/Contribute-6366F1?style=for-the-badge&logo=git&logoColor=white)](https://github.com/HafidIdrissi/Time-Tracker/contribute)
[![Report an issue](https://img.shields.io/badge/Report%20an%20issue-6366F1?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HafidIdrissi/Time-Tracker/issues)

</div>

> **Contributions are welcome** — documentation, testing, bug fixes and Windows improvements are
> great places to start. The repository ships a contributing guide, a code of conduct, issue and
> pull request templates, and a test suite that runs in CI.

## Selected projects

<table>
<tr>
<td width="50%" valign="top">

### Persona Studio

AI content and personal-branding SaaS: image and avatar generation, scene merging, video and
lipsync, with credit-based Stripe billing.

`Vite` · `Supabase` · `PostgreSQL/RLS` · `Deno` · `Stripe` · `fal.ai`

**Status:** Private code · in launch preparation

[influencepersona.com](https://influencepersona.com)

</td>
<td width="50%" valign="top">

### GoEditPDF

Privacy-first PDF editor running entirely in the browser — merge, annotate, sign, watermark,
redact and OCR, with no document ever uploaded to a server.

`JavaScript` · `PDF.js` · `PDF-Lib` · `Fabric.js` · `Tesseract.js`

**Status:** Live product

[goeditpdf.com](https://goeditpdf.com) · [source](https://github.com/HafidIdrissi/goeditpdf-public)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### LexiNegotiate

AI-assisted legal document analysis: reads a contract as text, image or PDF and returns a risk
score, clause comparison and negotiation strategies.

`React 19` · `TypeScript` · `Google GenAI SDK`

**Status:** Open source prototype

[source](https://github.com/HafidIdrissi/LexiNegotiate-) · [video demo](https://www.youtube.com/watch?v=dinw3NJyobc)

<sub>Decision-support tool; it does not replace legal advice.</sub>

</td>
<td width="50%" valign="top">

### Bayesian Battery SOH

Hierarchical Bayesian inference for the state of health of Li-ion batteries, comparing a
per-battery model against a fleet-level pooled model.

`Python` · `PyMC` · `NumPyro/JAX` · `ArviZ`

**Status:** Research

[source](https://github.com/HafidIdrissi/bayesian-soh-batteries)

<sub>Simulated dataset inspired by NASA PCoE; not validated on real cells.</sub>

</td>
</tr>
</table>

<details>
<summary><b>More projects</b></summary>

<br/>

| Project | What it is | Status |
|---|---|---|
| [smart-waste-detector-yolo](https://github.com/HafidIdrissi/smart-waste-detector-yolo) | Six-category waste detector, transfer-learned from Ultralytics YOLO. mAP50 0.496 after 30 epochs. | Open source |
| [cv-pdf-studio](https://github.com/HafidIdrissi/cv-pdf-studio) | Agent skill turning verified career evidence into CV and cover-letter PDFs, with provenance checks. | Open source |
| [humanizer](https://github.com/HafidIdrissi/humanizer) | Claude Code skill that strips AI writing patterns and rewrites text in a human voice, English and French. | Open source |
| [Devis-Chantier-AI](https://github.com/HafidIdrissi/Devis-Chantier-AI) | Turns a job description or a site photo into a structured construction quote, assisted by Gemini. | Open source |
| [expense-tracker](https://github.com/HafidIdrissi/expense-tracker) | Next.js expense tracker with a flexible daily budget and local persistence, no backend. | Open source |
| [CheckAI](https://checkai-app.com) | AI-text classification SaaS on a RoBERTa model served through Hugging Face, with Stripe billing. | Live product · private code |

</details>

## Background

I am a software engineer, trained at JUNIA in Lille where I earned a French *diplôme d'ingénieur*
carrying master's grade. I design and build **AI SaaS platforms** end to end — data model, backend,
authentication, billing, CI/CD and interface — most of them on my own. CheckAI, a text classification
service built on a RoBERTa model served through Hugging Face, is online today; Influence Persona, a
multimodal content platform on Supabase and Stripe, is in launch preparation.

My engineering background is industrial before it was commercial. At **Hager Group** I built a proof
of concept for deploying IoT APIs securely on Azure Kubernetes Service across three private virtual
networks. At **Mirion Technologies** I built a real-time 2D LiDAR and SLAM mapping prototype on
embedded Linux, with a Python operator interface. That work is why I care about systems that behave
predictably under constraint and keep their data where it belongs — the thesis at the top of this
page comes from it, not from marketing.

I keep an audited record of my own work. Several figures that used to sit on this page are gone,
because the repositories behind them did not support the claim.

| | |
|---|---|
| **Hager Group** · final-year internship | Cloud & IoT architecture, AKS proof of concept · 2024 |
| **Mirion Technologies** · R&D internship | Embedded systems, LiDAR SLAM and operator HMI · 2023 |
| **JUNIA / HEI**, Lille | *Diplôme d'ingénieur*, master's grade · 2019–2024 |

## Stack

| | |
|---|---|
| **Languages** | Python · TypeScript · C/C++ · C# · Java · Kotlin · SQL · Bash |
| **Frontend** | React · Next.js · Vite · Tailwind CSS |
| **Backend** | Node.js · Supabase · PostgreSQL · MongoDB · REST APIs · Stripe |
| **AI / Data** | PyTorch · Hugging Face · OpenCV · PyMC · LLM APIs (Claude, GPT, Gemini) |
| **Infrastructure** | Azure (AKS, DevOps) · Docker · Kubernetes · Terraform · GitHub Actions · GitLab CI |

## Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=HafidIdrissi&custom_title=Contribution%20activity&bg_color=0D1117&color=E2E8F0&title_color=F97316&line=F97316&point=6366F1&area=true&area_color=F97316&hide_border=true&radius=8" alt="Graph of my GitHub contribution activity over the last month" width="900" />

<br/><br/>

<!-- Regenerated every 12h by .github/workflows/snake.yml — source branch `output`, do not edit by hand -->
<img alt="A snake eating my GitHub contribution graph, animated" src="https://raw.githubusercontent.com/HafidIdrissi/HafidIdrissi/output/ocean.gif" width="900" />

</div>

---

<div align="center">

**Open to full-stack, cloud and AI engineering work — permanent or freelance, France and Europe.**

[![Portfolio](https://img.shields.io/badge/Portfolio-hidrissi.tech-F97316?style=for-the-badge&logo=googlechrome&logoColor=white)](https://hidrissi.tech)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hafid-idrissi/)
[![Email](https://img.shields.io/badge/Email-6366F1?style=for-the-badge&logo=gmail&logoColor=white)](mailto:idrissihafez@gmail.com)

<sub>If Time Tracker is useful to you, a ⭐ on the repository helps other people find it.</sub>

</div>
