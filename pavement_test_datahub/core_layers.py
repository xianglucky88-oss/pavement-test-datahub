"""对层界已完整确认的芯样计算逐层厚度。"""

from .contract import Row, apply_rows, index_rows, number, read_rows


def build_facts(data: Row) -> list[Row]:
    def measure(row: Row) -> Row:
        layers = []
        last_end = 0
        for key, layer in index_rows(read_rows(row, "layers"), "id").items():
            start = number(layer, "top_mm", minimum=0)
            end = number(layer, "bottom_mm", minimum=0)
            if start < last_end or end <= start:
                raise ValueError(f"invalid or overlapping layer: {key}")
            last_end = end
            layers.append({"layer": key, "thickness_mm": round(end - start, 6)})
        return {"layers": layers}

    return apply_rows(data, measure)
