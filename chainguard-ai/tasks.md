# ChainGuard AI — Task Tracker

Status legend: `[ ]` Not started · `[-]` In progress · `[x]` Complete · `[!]` Blocked

## Phase 1 — Repository and environment
- [x] Repository skeleton and directories
- [x] README.md, LICENSE, .gitignore, .env.example
- [x] prd.md, architecture.md, rules.md, design.md, tasks.md, memory.md
- [x] pyproject.toml, requirements.txt, frontend package.json, tsconfig, vite config
- [x] Makefile, Dockerfile, docker-compose.yml, CI workflow
- [x] config/logging/dependencies scaffolding

## Phase 2 — Data ingestion
- [x] Format detector (CSV/JSON/XML)
- [x] CSV parser (JSON-array and pipe-delimited array forms)
- [x] JSON parser (single object + array)
- [x] XML parser (nested element form, hardened)
- [x] Schema validator (required fields, ranges, types)
- [x] Normalizer (arrays, amounts, timestamps, ports)
- [x] Deduplicator (exact + txid-based)
- [x] Quality analyzer (quality score, per-record validation errors)
- [x] Synthetic demo data generator (seed 42, injected scenarios)

## Phase 3 — Storage
- [x] DuckDB store (parameterized queries, pagination)
- [x] Parquet store (normalized records per dataset)
- [x] Repositories (transactions/wallets/network/records)
- [x] Run/model/alert/feedback artifacts (JSON store)

## Phase 4 — Feature engineering
- [x] Transaction features
- [x] Wallet features
- [x] Temporal features
- [x] Network features
- [x] Graph features
- [x] Feature pipeline (FV-1.0, definition hash, caching)

## Phase 5 — Graph and temporal analysis
- [x] Graph builder (4 node kinds, 6 edge types, confidence)
- [x] Graph repository + bounded neighborhood queries
- [x] Temporal correlation (windows, exponential decay)
- [x] Sequence engine (multi-hop, rapid forwarding, peeling)

## Phase 6 — ML detection
- [x] BaseDetector abstraction
- [x] IsolationForest detector
- [x] Supervised detector (labels path)
- [x] Model registry (versions, metrics, artifacts)
- [x] Scoring (anomaly 0–100)

## Phase 7 — Evidence fusion
- [x] Evidence types + ID minting
- [x] Evidence fusion (categories, independence, strength 0–100)
- [x] Explanation builder (observed/baseline/contribution)
- [x] Counterfactuals ("What would change this?")
- [x] Trace builder (full evidence chain)

## Phase 8 — Alerts and API
- [x] Lead generator + prioritizer
- [x] Alert repository
- [x] FastAPI: health, datasets, analysis, runs, alerts, wallets, transactions, network, clusters, graph, metrics, feedback, reports
- [x] Report builders (JSON, CSV, PDF)

## Phase 9 — Frontend
- [x] Vite + React + TS scaffold, theme, layout, nav rail, context bar
- [x] Overview dashboard (metrics, charts, graph preview)
- [x] Data Intake (upload, validation stats, quality, errors)
- [x] Alerts table + filters
- [x] Investigation workspace (scores, why flagged, trace evidence, timeline, graph, technical, counterfactuals, feedback)
- [x] Transactions / Wallets / Network tables + drawers
- [x] Graph Analysis (Cytoscape, filters)
- [x] Clusters, Timeline, Model Performance, Data Quality, Reports, Settings pages
- [x] Evidence Explorer
- [x] Investigator/Analyst/Technical modes
- [x] Vitest component tests

## Phase 10 — Evidence tracing
- [x] Trace Evidence API + UI chain rendering
- [x] Edge details (type, timestamp, confidence, source, Δt)
- [x] Neighborhood expansion without full-graph load

## Phase 11 — Reports, feedback, reproducibility
- [x] JSON/CSV/PDF export with provenance + disclaimer
- [x] Analyst feedback persistence
- [x] Run metadata (run_id, dataset hash, versions, config)

## Phase 12 — Testing, Docker, CI, documentation
- [x] Backend unit tests (parsers, validation, features, temporal, graph, patterns, ML, fusion, explanations, reports)
- [x] Backend integration tests (CSV/JSON/XML → API → alerts → reports)
- [x] Frontend tests (vitest)
- [x] Docker + compose (documented; daemon unavailable on build host — verified natively)
- [x] GitHub Actions CI
- [x] docs/ (model card, threat model, scalability, ml-methodology, data-model, demo-script)
- [x] scripts: verify_installation, evaluate_models, run_ablation
- [x] Final quality gate executed
