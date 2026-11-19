"""用输入给定的参考高程计算两侧轮迹深度。"""

from .contract import Row, apply_rows, number


def build_facts(data: Row) -> list[Row]:
    def measure(row: Row) -> Row:
        return {"chainage_m": number(row, "chainage_m"),
                **{f"{side}_depth_mm": round(max(0, number(row, f"{side}_reference_mm") - number(row, f"{side}_observed_mm")), 6)
                   for side in ("left", "right")}}

    return apply_rows(data, measure)
