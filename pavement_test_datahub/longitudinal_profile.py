"""计算连续单车道纵断面的相邻高程差均方根。"""

from math import sqrt

from .contract import Row, apply_rows, index_rows, number, read_rows, text


def build_facts(data: Row) -> list[Row]:
    def measure(row: Row) -> Row:
        points = sorted(index_rows(read_rows(row, "points"), "id").values(), key=lambda point: number(point, "chainage_m"))
        distances = [number(point, "chainage_m") for point in points]
        if len(points) < 2 or len(set(distances)) != len(points):
            raise ValueError("at least two distinct chainage samples are required")
        heights = [number(point, "elevation_mm") for point in points]
        rms = sqrt(sum((right - left) ** 2 for left, right in zip(heights, heights[1:])) / (len(heights) - 1))
        return {"lane": text(row, "lane"), "start_m": distances[0], "end_m": distances[-1],
                "sample_count": len(points), "rms_step_mm": round(rms, 6)}

    return apply_rows(data, measure)
