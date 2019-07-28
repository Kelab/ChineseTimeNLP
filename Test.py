# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 10:21
# @Author  : zhm
# @File    : Test.py
# @Software: PyCharm
# @Changed : tianyuningmou

from TimeNormalizer import TimeNormalizer  # 引入包

tn = TimeNormalizer(isPreferFuture=False)

res = tn.parse(target=u'星期天晚上')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
