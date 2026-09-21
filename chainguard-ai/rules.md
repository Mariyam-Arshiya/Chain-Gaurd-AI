# ChainGuard AI — Coding Rules

- Python **3.11+** (repo verified on 3.12); TypeScript **strict** mode.
- **Pydantic** models for all API schemas; dataclasses/TypedDicts internally where lighter.
- Small focused modules; one responsibility per file; no giant files.
- **No hidden global state** — application state is an injected `AppState`.
- **No hard-coded analytical thresholds** — temporal windows, pattern limits, score weights, and caps live in `config.py` with documented defaults; per-run configuration is recorded in run metadata.
- No fake API responses, no mock data paths, no unused dependencies, no dead code, no unused imports.
- No silent data loss: invalid records are reported with record number, field, error type, human explanation, raw preview, severity.
- No uncaught exceptions in request handlers; user-facing errors are structured JSON without stack traces.
- All core functions have deterministic tests; fixtures use fixed seeds.
- All model outputs carry provenance: model_name, model_version, feature_version, run_id.
- Analytical language is qualified: Investigative Lead / Risk Signal / Observed Association — never Criminal / Guilty / Proven.
- Type hints on all public functions; docstrings on module boundaries.
- Monospace identifiers (txid, wallet, IP, hash, run ID) render as monospace in the UI.
- Every raw-value output includes the disclaimer where analytical claims appear.
