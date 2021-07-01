from typing import List, Optional, Union

import arrow
from arrow.arrow import Arrow
from loguru import logger

from .helpers.str_common import (
    del_keyword,
    filter_irregular_expression,
    number_translator,
)
from .point import TimePoint
from .result import DeltaType, Result
from .unit import TimeUnit


# 时间表达式识别的主要工作类
class TimeNormalizer:
    def __init__(self, isPreferFuture=True, tz="Asia/Shanghai", pattern=None):
        self.isPreferFuture = isPreferFuture
        if pattern is None:
            from .resource.pattern import pattern

        self.tz = tz
        self.pattern = pattern

    def parse(self, target: str, baseTime: Union[arrow.Arrow, str] = None) -> dict:
        """
        TimeNormalizer的构造方法，baseTime取默认的系统当前时间
        :param baseTime: 基准时间点
        :param target: 待分析字符串
        :return: 时间单元数组
        """
        if baseTime is None:
            baseTime = arrow.now(self.tz)

        logger.debug(f"目标字符串: {target}")

        self.isTimeDelta = False
        self.timeDelta = None  # type: Optional[DeltaType]
        self.target = target
        self.baseTime: Arrow = arrow.get(baseTime)
        self._baseTime = self.baseTime
        return self.extract()

    def pre(self):
        """
        待匹配字符串的清理空白符和语气助词以及大写数字转化的预处理
        """
        self.target = filter_irregular_expression(self.target)
        self.target = del_keyword(self.target, r"\s+")  # 清理空白符
        self.target = del_keyword(self.target, "[的]+")  # 清理语气助词
        self.target = number_translator(self.target)  # 大写数字转化
        logger.debug(f"清理空白符和语气助词以及大写数字转化的预处理 {self.target}")

    def extract(self) -> dict:
        """返回 TimeUnit[] 时间表达式类型数组"""
        self.pre()
        startline = -1
        endline = -1
        rpointer = 0
        temp = []
        match = self.pattern.finditer(self.target)
        logger.debug("=======")
        logger.debug("用正则提取关键字：")
        for m in match:
            logger.debug(m)
            startline = m.start()
            if startline == endline:
                rpointer -= 1
                temp[rpointer] = temp[rpointer] + m.group()
            else:
                temp.append(m.group())
            logger.debug(f"temp：{temp}")
            endline = m.end()
            rpointer += 1
        logger.debug("=======")

        try:
            res: List[TimeUnit] = []
            # 时间上下文： 前一个识别出来的时间会是下一个时间的上下文，用于处理：周六3点到5点这样的多个时间的识别，第二个5点应识别到是周六的。
            contextTp = TimePoint()

            logger.debug(f"基础时间： {self.baseTime}")
            logger.debug(f"待处理的字段: {temp}")
            logger.debug(f"待处理字段长度: {rpointer}")
            for i in range(0, rpointer):
                # 这里是一个类嵌套了一个类
                res.append(TimeUnit(temp[i], self, contextTp))
                contextTp = res[i].tp

            logger.debug(f"全部字段处理后的结果： {res}")
            res = self.filter(res)

            if self.isTimeDelta and self.timeDelta:
                return Result.from_timedelta(self.timeDelta)
            if len(res) == 1:
                return Result.from_timestamp(res)
            if len(res) == 2:
                return Result.from_timespan(res)
            return Result.from_invalid()
        except Exception as e:
            logger.opt(exception=e).debug("解析时发生错误")
            return Result.from_exception(e)

    def filter(self, tu_arr: List[TimeUnit]):
        """
        过滤掉无效识别。
        """
        res = []
        for tu in tu_arr:
            if not tu:
                continue

            if tu.time.int_timestamp != 0:
                res.append(tu)
        logger.debug(f"过滤无效识别后： {res}")
        return res
