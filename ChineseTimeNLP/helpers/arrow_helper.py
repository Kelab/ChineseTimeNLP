from typing import List

from arrow import Arrow


def arrow2tp(i: Arrow) -> List[int]:
    return [i.year, i.month, i.day, i.hour, i.minute, i.second]


def tp2arrow(tp: List[int]) -> Arrow:
    return Arrow(*tp)
