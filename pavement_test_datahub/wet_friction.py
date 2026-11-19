"""保存单一湿态试验的摩擦读数和阈值判定。"""

from .contract import Row, apply_rows, number, text


def build_facts(data: Row) -> list[Row]:
    limit = number(data, "minimum_coefficient", minimum=0)

    def measure(row: Row) -> Row:
        coefficient = number(row, "coefficient", minimum=0)
        return {"run": text(row, "run"), "chainage_m": number(row, "chainage_m"),
                "coefficient": coefficient, "meets_minimum": coefficient >= limit}

    return apply_rows(data, measure)
