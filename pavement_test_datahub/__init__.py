"""路面试验成果"""

from . import longitudinal_profile, transverse_ruts, wet_friction, fwd_deflection, core_layers
from .contract import Row

PIPELINES = {
    "longitudinal-profile": longitudinal_profile.build_facts,
    "transverse-ruts": transverse_ruts.build_facts,
    "wet-friction": wet_friction.build_facts,
    "fwd-deflection": fwd_deflection.build_facts,
    "core-layers": core_layers.build_facts,
}


def process(pipeline: str, data: Row) -> list[Row]:
    """Validate and transform an independent input dataset into keyed facts."""
    if pipeline not in PIPELINES:
        raise ValueError(f"unknown pipeline: {pipeline}")
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    return PIPELINES[pipeline](data)
