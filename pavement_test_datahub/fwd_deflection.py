"""将落锤冲击的中心读数按荷载档分组并计算均值。"""

from collections import defaultdict
from statistics import mean

from .contract import Row, index_rows, number, read_rows, text


def build_facts(data: Row) -> list[Row]:
    groups = defaultdict(list)
    for key, row in index_rows(read_rows(data), "id").items():
        group = (text(row, "point"), number(row, "load_kn", minimum=0))
        groups[group].append((key, number(row, "center_deflection_um", minimum=0)))
    return [{"fact_id": f"{point}@{load}", "point": point, "load_kn": load,
             "mean_center_um": round(mean(reading for _, reading in drops), 6),
             "drops": sorted(key for key, _ in drops)} for (point, load), drops in sorted(groups.items())]
