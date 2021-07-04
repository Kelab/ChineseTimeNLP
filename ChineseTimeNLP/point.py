from arrow import Arrow

from .helpers.arrow_helper import arrow2tp
from .result import DeltaType


class TimePoint:
    """
    时间表达式单元规范化对应的内部类,对应时间表达式规范化的每个字段。\n
    六个字段分别是：年-月-日-时-分-秒 \n
    每个字段初始化为-1
    """

    def __init__(self):
        #             0年 1月 2日 3时 4分 5秒
        self.tunit = [-1, -1, -1, -1, -1, -1]

    def copy(self) -> "TimePoint":
        new_instance = TimePoint()
        new_instance.tunit = self.tunit.copy()
        return new_instance

    @property
    def year(self) -> int:
        return self.tunit[0]

    @year.setter
    def year(self, value: int):
        self.tunit[0] = value

    @property
    def month(self) -> int:
        return self.tunit[1]

    @month.setter
    def month(self, value: int):
        self.tunit[1] = value

    @property
    def day(self) -> int:
        return self.tunit[2]

    @day.setter
    def day(self, value: int):
        self.tunit[2] = value

    @property
    def hour(self) -> int:
        return self.tunit[3]

    @hour.setter
    def hour(self, value: int):
        self.tunit[3] = value

    @property
    def minute(self) -> int:
        return self.tunit[4]

    @minute.setter
    def minute(self, value: int):
        self.tunit[4] = value

    @property
    def second(self) -> int:
        return self.tunit[5]

    @second.setter
    def second(self, value: int):
        self.tunit[5] = value

    def is_valid(self):
        """只要有一个 unit 大于 0，就说明有效"""
        for i in self.tunit:
            if i >= 0:
                return True
        return False

    def gen_delta(self) -> DeltaType:
        return {
            "year": max(self.year, 0),
            "month": max(self.month, 0),
            "day": max(self.day, 0),
            "hour": max(self.hour, 0),
            "minute": max(self.minute, 0),
            "second": max(self.second, 0),
        }

    def get_arrow(self) -> Arrow:
        year = max(self.year, 1)
        month = max(self.month, 1)
        day = max(self.day, 1)
        hour = max(self.hour, 0)
        minute = max(self.minute, 0)
        second = max(self.second, 0)
        return Arrow(year, month, day, hour, minute, second)

    def set_unit(self, arrow: Arrow):
        self.tunit = arrow2tp(arrow)

    def __repr__(self) -> str:
        return str(self.tunit)
