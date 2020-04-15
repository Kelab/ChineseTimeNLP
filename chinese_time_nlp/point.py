from arrow import Arrow
from .helpers.int_common import not_neg_number


class TimePoint:
    """
    时间表达式单元规范化对应的内部类,对应时间表达式规范化的每个字段。\n
    六个字段分别是：年-月-日-时-分-秒 \n
    每个字段初始化为-1
    """

    def __init__(self):
        #             0年 1月 2日 3时 4分 5秒
        self.tunit = [-1, -1, -1, -1, -1, -1]

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

    def get_today_seconds(self):
        hour = not_neg_number(self.hour)
        minute = not_neg_number(self.minute)
        second = not_neg_number(self.second)
        return hour * 3600 + minute * 60 + second

    def get_arrow(self) -> Arrow:
        year = not_neg_number(self.year)
        month = not_neg_number(self.month)
        day = not_neg_number(self.day)
        hour = not_neg_number(self.hour)
        minute = not_neg_number(self.minute)
        second = not_neg_number(self.second)
        return Arrow(year, month, day, hour, minute, second)

    def __repr__(self) -> str:
        return str(self.tunit)
