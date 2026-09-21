# ChainGuard AI — Project Memory

## Product decisions
- Offline-first, single FastAPI backend + React/Vite frontend; no external AI APIs.
- Two independent scores: **Anomaly Score** (unusualness) and **Evidence Strength** (supporting evidence) — never "probability of guilt".
- The judge-demo moment is **TRACE EVIDENCE**: full clickable chain from network observation to lead.
- Graph: NetworkX prototype behind `GraphRepository` interface for later graph-DB migration.
- Storage: DuckDB for queries, Parquet for reproducible artifacts, JSON artifacts for runs/models/alerts/feedback.
- Evidence categories: TRANSACTION, WALLET, TEMPORAL, GRAPH, NETWORK, SEQUENCE, ML.
- Feature version **FV-1.0**; model versions **IF-v1.0** (IsolationForest), **SUP-v1.0** (supervised).

## Dataset schema
Logical fields (all formats): `timestamp, src_ip, dst_ip, src_port, dst_port, txid, input_addresses[], output_addresses[], input_amounts[], output_amounts[], fee, script_type, geo_country, asn`.
- CSV arrays: JSON style `["a","b"]` or pipe style `a|b`.
- XML arrays: repeated `<address>` / `<amount>` children.
- `script_type` ∈ P2PKH, P2SH, P2WPKH, P2WSH, P2TR, NONSTANDARD (unknown → warning, allowed).

## Configuration defaults (config.py)
`temporal_window_seconds: 30` · `temporal_windows: [1,5,30,300,1800]` · `max_hops: 2 (cap 4)` · `upload_max_mb: 250` · `demo_max_records: 1,000,000` · `if_n_estimators: 200` · `contamination: auto` · `random_state/seed: 42` · weights: ml 0.35, patterns 0.25, graph 0.15, temporal 0.15, network 0.10 · evidence-strength weights: category_count 0.4, independence 0.2, completeness 0.15, confidence 0.15, consistency 0.1.

## Architecture (as built)
- `backend/app/ingestion`: format_detector, csv_parser, json_parser, xml_parser, schema_validator, normalizer, deduplicator, quality
- `backend/app/storage`: duckdb_store, parquet_store, repositories, artifact_store
- `backend/app/features`: 5 feature modules + feature_pipeline (FV-1.0, definition hash)
- `backend/app/graph`: graph_builder, graph_repository (NetworkX), subgraph_service
- `backend/app/temporal`: windows/correlation, sequence_engine
- `backend/app/detection`: base_detector, isolation_forest_detector, supervised_detector, model_registry, scoring
- `backend/app/patterns`: fan_in, fan_out, multi_hop, rapid_forwarding, splitting, consolidation, peeling_chain
- `backend/app/evidence`: evidence_types, evidence_fusion, explanation, counterfactuals, trace_builder
- `backend/app/clustering`: clustering_service (DBSCAN), cluster_profiles
- `backend/app/alerts`: lead_generator, prioritizer, alert_repository
- `backend/app/reports`: json_report, csv_report, pdf_report
- `backend/app/api`: 13 routers; `app/pipeline.py` orchestrates a full run

## Model versions
- IF-v1.0: IsolationForest(n_estimators=200, contamination="auto", random_state=42) on wallet+transaction+graph features.
- SUP-v1.0: RandomForestClassifier when labels present in dataset (synthetic generator writes labels).

## Known limitations
- Docker daemon unavailable on the build host (Windows/Git Bash): Docker files + CI provided, native path verified. Linux build expected to work unchanged.
- GeoIP optional; no mmdb bundled (licensing) — graceful "GeoIP enrichment unavailable".
- Betweenness approximated (k-sample) above 20k nodes for performance.
- PDF report uses reportlab-free custom minimal PDF writer (no extra dependency); text-based forensic report.
- Feedback does not auto-retrain the model; explicitly labeled "Feedback available for next training cycle".
- Evaluation metrics are **synthetic evaluation** only.

## Failed approaches / corrections
- Initial plan relied on Docker for verification; Docker Desktop not running on host → added native pipeline runner + verification script; Docker kept for Linux deployment.
- Avoided third-party PDF libs to keep the dependency surface minimal and offline-installable.

## Completed milestones
- Phase 1–12 implemented; see tasks.md for the full checklist.
