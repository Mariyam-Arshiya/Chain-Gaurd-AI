# ChainGuard AI — Product Requirements Document

## 1. Product Vision

ChainGuard AI is an **offline, explainable, cross-layer** forensic analysis platform for Bitcoin transaction/network metadata. It ingests bulk CSV/JSON/XML observations, correlates network-layer signals (IP/port/timing/geo/ASN) with blockchain-layer signals (wallets, TXIDs, amounts, fees, script types), applies machine-learning anomaly detection, and produces **ranked, evidence-backed investigative leads** with full traceability.

**Tagline:** From Bitcoin Signals to Traceable Evidence.
**Core promise:** Upload → Validate → Correlate → Detect → Explain → Trace → Review → Report.

## 2. Problem Statement (SIH)

**AI-Powered Monitoring & Analysis of Bitcoin Transaction Traffic** — Bitcoin's pseudonymous, peer-to-peer design lets criminal actors move, layer, and cash out illicit funds — ransomware payments, darknet-market proceeds, extortion, and laundering — while evading traditional financial surveillance.

**Objective:** Design and build a complete **offline** system that ingests bulk Bitcoin transaction/network metadata (CSV/JSON/XML), correlates network-layer observations with blockchain-layer data, and applies AI/ML to detect anomalies, cluster entities, and generate prioritized, explainable investigative leads.

## 3. Target Users

- Law-enforcement / cyber-forensics investigators
- Financial-crime analysts (internal review teams)
- Technical forensic engineers (reproducibility, model governance)

## 4. Personas

| Persona | Needs | Mode |
|---|---|---|
| **Investigator Ira** | Plain-language answers: what happened, why flagged, what evidence, what would change it | Investigator Mode |
| **Analyst Ada** | Feature values, baselines, graph metrics, clusters, temporal patterns | Analyst Mode |
| **Engineer Theo** | Model/feature versions, run IDs, dataset hashes, inference timing, logs | Technical Mode |

## 5. User Journeys

### Journey A — Ingest & validate
1. User opens **Data Intake**, uploads CSV/JSON/XML (≤ configurable size cap).
2. System detects format, parses, validates, normalizes, dedups, reports quality.
3. User reviews validation statistics and per-record errors (nothing silently dropped).

### Journey B — Analyze & investigate
1. User runs analysis; pipeline stages stream progress.
2. **Alerts** lists ranked leads (Anomaly Score + Evidence Strength + Priority).
3. User opens a lead → **Investigation Workspace** → WHY FLAGGED?, TRACE EVIDENCE, timeline, graph, counterfactuals.
4. User records feedback (Relevant / False Positive / Needs Review + note).

### Journey C — Report
1. User exports lead(s) as JSON/CSV/PDF with full provenance and disclaimer.

## 6. Functional Requirements

- FR1 Ingest CSV/JSON/XML with required fields: `timestamp`, `src_ip`, `dst_ip`, `src_port`, `dst_port`, `txid`, `input_addresses[]`, `output_addresses[]`, `input_amounts[]`, `output_amounts[]`, `fee`, `script_type`, `geo_country`, `asn`.
- FR2 Format detection, schema validation, normalization, deduplication, quality scoring; invalid records stored with record number, field, error type, explanation, raw preview, severity.
- FR3 Storage in DuckDB (query) + Parquet (normalized artifacts).
- FR4 Feature engineering with version (FV-1.0) and definition hash across transaction/wallet/temporal/network/graph groups.
- FR5 Graph model (Wallet, Transaction, IP, NetworkObservation) with edge types INPUT_TO, OUTPUT_TO, OBSERVED_ON, CONNECTED_TO, SAME_COUNTERPARTY, TEMPORALLY_ASSOCIATED; graph metrics (degree, betweenness, clustering coefficient, component size).
- FR6 Temporal correlation with configurable windows (default 30 s) and exponential-decay confidence.
- FR7 ML anomaly detection via `BaseDetector` abstraction (IsolationForest default; supervised when labels exist; LOF/OC-SVM optional comparators).
- FR8 Flow-pattern modules: fan-in, fan-out, multi-hop, rapid forwarding, splitting, consolidation, peeling-chain-like.
- FR9 Behavioral clustering (DBSCAN; HDBSCAN when available) with behavior profiles.
- FR10 Evidence fusion across TRANSACTION, WALLET, TEMPORAL, GRAPH, NETWORK, SEQUENCE, ML categories → two scores (Anomaly 0–100, Evidence Strength 0–100) + priority.
- FR11 Explainability: per-feature observed/baseline/contribution with source records; SHAP-compatible; counterfactual "What would change this?".
- FR12 Trace Evidence: clickable chain from transaction → wallet → counterparties → network observation → temporal relation → flow pattern → ML signal → fused evidence → lead; bounded graph neighborhood expansion.
- FR13 Alerts API with pagination/filter/sort; investigation workspace data; timeline.
- FR14 Analyst feedback (local persistence; "Feedback available for next training cycle").
- FR15 Reports: JSON, CSV, PDF with full provenance and disclaimer.
- FR16 Reproducible runs: run_id, dataset_id, dataset_sha256, model/version, feature version, configuration, software version.
- FR17 Dashboards: Overview, Data Intake, Alerts, Evidence Explorer, Transactions, Wallets, Network, Graph Analysis, Clusters, Timeline, Model Performance, Data Quality, Reports, Settings.
- FR18 Investigation modes: Investigator / Analyst / Technical.
- FR19 Synthetic deterministic demo dataset generator (seed 42) with injected pattern scenarios.

## 7. Non-Functional Requirements

- Offline-first; no external AI/blockchain/CDN/telemetry.
- Responsive dark forensic UI, dense information design, accessible (labels, focus, reduced motion).
- Deterministic behavior given seeds; structured logging; no raw stack traces in UI.
- Test coverage on all core functions; CI gate.

## 8. Acceptance Criteria

- CSV/JSON/XML ingestion of demo datasets yields valid normalized tables + quality report.
- A full run produces ranked alerts with anomaly score, evidence strength, priority, primary signal, model/feature versions.
- Every alert exposes explanation + counterfactuals + traceable evidence chain.
- Reports export in JSON/CSV/PDF including disclaimer.
- `make demo` boots backend+frontend, prints run ID and lead count; UI shows OFFLINE MODE banner and disclaimer.
- Backend unit+integration tests, frontend tests, typecheck, build all pass.

## 9. Security Requirements

Upload caps (default 250 MB, configurable), extension/MIME validation, safe temp storage, path-traversal protection, parameterized queries, safe XML parsing (entity-expansion safe), no execution of uploads, request validation, local-only CORS, no telemetry.

## 10. Offline Requirements

No internet at runtime. Optional GeoIP via local `data/geoip/GeoLite2-Country.mmdb`; if missing show "GeoIP enrichment unavailable" and continue. All assets served locally; production frontend build served by the backend or local static server.

## 11. Data Policy

- Only user-supplied or locally generated synthetic data.
- No real seized or live-intercepted data.
- All data stored locally under `backend/storage/` and `data/`.
- Nothing is uploaded to any external service.
- Deleting a dataset removes its local artifacts.

## 12. Ethical Boundaries

Permitted vocabulary: Investigative Lead, Anomaly, Risk Signal, Observed Association, Evidence, Needs Review, Suspicious Flow Pattern, Temporal Association, Analytical Priority.
Forbidden (unless explicit dataset labels): Criminal, Guilty, Confirmed Launderer, Real Owner, Identified Criminal, Proven Illicit Activity.
Every relevant screen shows: *"Analytical signals and observed relationships do not independently establish criminal activity or real-world identity. Human review is required."*

## 13. Demo Flow

See README "SIH demo flow" and `docs/demo-script.md`; the judge moment is **TRACE EVIDENCE**.

## 14. Future Scope

Graph DB backend, streaming ingestion, active-learning retraining loop (implemented & tested), multi-dataset federation, entity resolution improvements, HDBSCAN.
