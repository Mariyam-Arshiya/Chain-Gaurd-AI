# ChainGuard AI — Design Document

## Direction

Professional **dark forensic-analysis** interface: dense, calm, precise. Not a generic SaaS admin template. Minimal animation, strong hierarchy, thin borders, compact controls, high information density.

## Palette (CSS variables, `frontend/src/styles/theme.css`)

```css
--bg: #0b0f14;
--surface: #111820;
--surface-raised: #17212b;
--border: #283541;
--text: #e9eff5;
--text-muted: #8b9aa8;
--cyan: #50d5e8;
--amber: #f4b860;
--red: #ef6b73;
--green: #62c995;
--blue: #6ea8ff;
```

Accents are restrained: cyan = interactive/selected, amber = attention/priority, red = high-priority alerts, green = healthy/normal, blue = informational.

## Typography

- UI: system sans stack (`Inter, "Segoe UI", system-ui, sans-serif`).
- Technical identifiers (TXIDs, wallet addresses, IPs, hashes, model/run IDs): monospace (`"JetBrains Mono", "Fira Code", Consolas, monospace`) with `.mono` class.

## Layout

- **Fixed left navigation rail** (56px, icon + label, collapsible) — sections: Overview, Data Intake, Alerts, Evidence Explorer, Transactions, Wallets, Network, Graph Analysis, Clusters, Timeline, Model Performance, Data Quality, Reports, Settings.
- **Top context bar**: mode badge (DEMO MODE / DATASET MODE), OFFLINE MODE chip, current dataset + run, investigation-mode switcher (Investigator/Analyst/Technical).
- **Main workspace**: dense tables, compact metric strips, split-screen investigation layout.
- **Right-side evidence drawer / inspection panel** for entity/evidence detail.

## Component rules

- Tables: 12px rows, thin `--border` separators, sticky headers, zebra-free, hover row highlight.
- Metric strip: compact stat blocks (value + label), no oversized cards.
- Score bars: 0–100 horizontal bars with numeric label; amber/red gradients by band.
- Graph: Cytoscape canvas on `--surface`, nodes sized by degree, edge labels on hover.
- Buttons: compact, 1px border, primary = cyan on dark.
- Focus states: 2px cyan outline; keyboard navigable; reduced-motion honored (`prefers-reduced-motion`).
- Text labels accompany color in every status indicator.

## Screens

1. **Overview** — metric strip (transactions, wallets, network observations, clusters, leads, high-priority, data-quality, avg inference ms), alert distribution, activity timeline, top entities, evidence-category distribution, compact graph preview.
2. **Data Intake** — upload zone (CSV/JSON/XML), caps, format detection, validation stats, quality panel, error table (record #, field, type, explanation, preview, severity).
3. **Alerts** — ranked lead table (Lead ID, Entity, Type, Anomaly, Evidence, Priority, Primary Signal, Timestamp, Status) → click opens Investigation.
4. **Investigation Workspace** — score strip (Anomaly / Evidence / Priority / Status); sections: WHY FLAGGED?, TRACE EVIDENCE, TIMELINE, RELATIONSHIP GRAPH, TECHNICAL EVIDENCE, WHAT WOULD CHANGE THIS?, ANALYST REVIEW.
5. **Evidence Explorer** — search evidence by ID/category/entity; view relationship details.
6. **Transactions / Wallets / Network** — dense paginated tables + detail drawer.
7. **Graph Analysis** — Cytoscape graph, entity search, hop/edge-type/confidence filters.
8. **Clusters** — behavioral cluster cards + member table.
9. **Timeline** — global + per-alert activity timeline.
10. **Model Performance** — model versions, metrics, inference time, evaluation summary.
11. **Data Quality** — dataset quality score, error/warning breakdown.
12. **Reports** — export panel + report history.
13. **Settings** — configuration values (temporal window, hops, caps), mode display.

## Disclaimers

Small footer on every screen: *"Analytical signals and observed relationships do not independently establish criminal activity or real-world identity. Human review is required."* + OFFLINE MODE note on context bar.

## Explicitly avoided

Purple gradients, neon cyberpunk decoration, oversized cards, fake 3D, decorative AI imagery, glassmorphism.
