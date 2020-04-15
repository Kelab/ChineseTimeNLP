from typing import List
from arrow import Arrow, get


def arrow2grid(arrow_ins: Arrow) -> List[str]:
    return arrow_ins.format("YYYY-M-D-H-m-s").split("-")


def grid2arrow(str_list: List[str]) -> Arrow:
    return get("-".join(str_list), "YYYY-M-D-H-m-s")
