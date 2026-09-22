"""Central configuration for ChainGuard AI.

All analytical thresholds/weights live here. Per-run configuration is recorded
in run metadata for reproducibility.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]


def _env(key: str, default: str) -> str:
    return os.environ.get(key, default)


@dataclass
class AppConfig:
    """Application configuration. All thresholds are configurable."""

    # Server
    host: str = _env("CG_HOST", "127.0.0.1")
    port: int = int(_env("CG_PORT", "8000"))

    # Paths
    storage_dir: Path = REPO_ROOT / "backend" / "storage"
    data_dir: Path = REPO_ROOT / "data"
    uploads_dir: Path = REPO_ROOT / "data" / "uploads"
    generated_dir: Path = REPO_ROOT / "data" / "generated"
    geoip_path: Path = REPO_ROOT / "data" / "geoip" / "GeoLite2-Country.mmdb"
    artifacts_dir: Path = REPO_ROOT / "backend" / "storage" / "artifacts"
    parquet_dir: Path = REPO_ROOT / "backend" / "storage" / "parquet"

    # Upload limits
    upload_max_mb: int = int(_env("CG_UPLOAD_MAX_MB", "250"))
    demo_max_records: int = int(_env("CG_DEMO_MAX_RECORDS", "1000000"))

    # Ingestion
    supported_formats: tuple[str, ...] = ("csv", "json", "xml")
    allowed_extensions: tuple[str, ...] = (".csv", ".json", ".xml")
    allowed_mime_prefixes: tuple[str, ...] = (
        "text/",
        "application/json",
        "application/xml",
        "text/xml",
        "application/octet-stream",  # browsers often send this for uploads
    )

    # Analysis
    temporal_window_seconds: int = int(_env("CG_TEMPORAL_WINDOW_SECONDS", "30"))
    temporal_windows: tuple[int, ...] = (1, 5, 30, 300, 1800)
    temporal_decay_tau: float = 10.0  # seconds; confidence = exp(-dt/tau)
    max_hops: int = int(_env("CG_MAX_HOPS", "2"))
    max_hops_cap: int = 4
    neighborhood_max_nodes: int = 400
    random_seed: int = int(_env("CG_RANDOM_SEED", "42"))

    # ML
    if_n_estimators: int = 200
    if_contamination: str | float = "auto"
    if_random_state: int = 42
    anomaly_score_cap: int = 100

    # Scoring weights (anomaly contribution mix; sum normalized in code)
    weight_ml: float = 0.35
    weight_patterns: float = 0.25
    weight_graph: float = 0.15
    weight_temporal: float = 0.15
    weight_network: float = 0.10

    # Evidence-strength weights
    weight_category_count: float = 0.40
    weight_independence: float = 0.20
    weight_completeness: float = 0.15
    weight_confidence: float = 0.15
    weight_consistency: float = 0.10

    # Pattern detection limits
    rapid_forwarding_window_seconds: int = 600
    rapid_forwarding_min_hops: int = 3
    fan_in_min_sources: int = 5
    fan_out_min_targets: int = 5
    peeling_min_hops: int = 3
    peeling_amount_decay: float = 0.55  # each hop retains < 55% of prior amount
    splitting_ratio: float = 0.35  # outputs smaller than 35% of input
    consolidation_ratio: float = 2.5  # output total >= 2.5x mean input
    betweenness_sample_threshold: int = 20000
    betweenness_pivots: int = 256
    dbscan_eps: float = 1.8
    dbscan_min_samples: int = 5

    # Behaviour
    demo_mode: bool = _env("CG_DEMO_MODE", "1") == "1"

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        return {k: str(v) if isinstance(v, Path) else v for k, v in d.items()}

    def analysis_config(self) -> dict[str, Any]:
        return {
            "temporal_window_seconds": self.temporal_window_seconds,
            "temporal_windows": list(self.temporal_windows),
            "temporal_decay_tau": self.temporal_decay_tau,
            "max_hops": self.max_hops,
            "random_seed": self.random_seed,
            "if_n_estimators": self.if_n_estimators,
            "if_contamination": self.if_contamination,
            "weight_ml": self.weight_ml,
            "weight_patterns": self.weight_patterns,
            "weight_graph": self.weight_graph,
            "weight_temporal": self.weight_temporal,
            "weight_network": self.weight_network,
        }


CONFIG = AppConfig()

DISCLAIMER = (
    "Analytical signals and observed relationships do not independently establish "
    "criminal activity or real-world identity. Human review is required."
)
REPORT_DISCLAIMER = (
    "This report presents analytical signals and observed relationships. It does not "
    "independently establish criminal activity or real-world identity."
)

FEATURE_VERSION = "FV-1.0"
MODEL_VERSION_IF = "IF-v1.0"
MODEL_VERSION_SUP = "SUP-v1.0"
SOFTWARE_VERSION = "1.0.0"
