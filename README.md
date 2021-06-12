# ChineseTimeNLP

[![PyPI](https://img.shields.io/pypi/v/ChineseTimeNLP.svg)](https://pypi.python.org/pypi/ChineseTimeNLP)
![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Downloads](https://pepy.tech/badge/chinesetimenlp)](https://pepy.tech/project/chinesetimenlp)
[![Downloads](https://pepy.tech/badge/chinesetimenlp/week)](https://pepy.tech/project/chinesetimenlp)

## 简介

这是 Time-NLP 的 Python3 版本。  
fork 自 [zhanzecheng/Time_NLP](https://github.com/zhanzecheng/Time_NLP)  

相关链接：

- Python2 版本 <https://github.com/ryanInf/Time-NLPY/tree/Python2%E7%89%88%E6%9C%AC>
- Python3 版本 <https://github.com/ryanInf/Time-NLPY>
- Java 版本 <https://github.com/shinyke/Time-NLP>
- PHP 版本 <https://github.com/crazywhalecc/Time-NLP-PHP>

## 配置

可以传入自定义的 pattern，默认 pattern 也可以通过 `from ChineseTimeNLP import pattern` 导入。

```py
TimeNormalizer(isPreferFuture=True, pattern=None):
```

对于下午两点、晚上十点这样的词汇，在不特别指明的情况下，默认返回明天的时间点。

## 安装使用

安装：

```bash
pip install ChineseTimeNLP
```

使用:

```py
from ChineseTimeNLP import TimeNormalizer
tn = TimeNormalizer()
res = tn.parse(target=u"三天后")  # target 为待分析语句，baseTime 为基准时间默认是当前时间
print(res)
```
## 功能说明

用于句子中时间词的抽取和转换  
详情请见 `Test.py`

```py
tn = TimeNormalizer(isPreferFuture=False)

res = tn.parse(target=u'星期天晚上')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(target=u'晚上8点到上午10点之间')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(
    target=u'2013年二月二十八日下午四点三十分二十九秒',
    baseTime='2013-02-28 16:30:29')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(
    target=u'我需要大概33天2分钟四秒',
    baseTime='2013-02-28 16:30:29')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(target=u'今年儿童节晚上九点一刻')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(target=u'三日')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(target=u'7点4')  # target为待分析语句，baseTime为基准时间默认是当前时间
print(res)
print('====')

res = tn.parse(target=u'今年春分')
print(res)
print('====')

res = tn.parse(target=u'7000万')
print(res)
print('====')

res = tn.parse(target=u'7百')
print(res)
print('====')

res = tn.parse(target=u'7千')
print(res)
print('====')

```

结果：

```sh
目标字符串:  星期天晚上
基础时间 2019-7-28-15-47-27
temp ['星期7晚上']
{"type": "timestamp", "timestamp": "2019-07-28 20:00:00"}
====
目标字符串:  晚上8点到上午10点之间
基础时间 2019-7-28-15-47-27
temp ['晚上8点', '上午10点']
{"type": "timespan", "timespan": ["2019-07-28 20:00:00", "2019-07-28 10:00:00"]}
====
目标字符串:  2013年二月二十八日下午四点三十分二十九秒
基础时间 2013-2-28-16-30-29
temp ['2013年2月28日下午4点30分29秒']
{"type": "timestamp", "timestamp": "2013-02-28 16:30:29"}
====
目标字符串:  我需要大概33天2分钟四秒
基础时间 2013-2-28-16-30-29
temp ['33天2分钟4秒']
timedelta:  33 days, 0:02:04
{"type": "timedelta", "timedelta": {"year": 0, "month": 1, "day": 3, "hour": 0, "minute": 2, "second": 4}}
====
目标字符串:  今年儿童节晚上九点一刻
基础时间 2019-7-28-15-47-27
temp ['今年儿童节晚上9点1刻']
{"type": "timestamp", "timestamp": "2019-06-01 21:15:00"}
====
目标字符串:  三日
基础时间 2019-7-28-15-47-27
temp ['3日']
{"type": "timestamp", "timestamp": "2019-07-03 00:00:00"}
====
目标字符串:  7点4
基础时间 2019-7-28-15-47-27
temp ['7点4']
{"type": "timestamp", "timestamp": "2019-07-28 07:04:00"}
====
目标字符串:  今年春分
基础时间 2019-7-28-15-47-27
temp ['今年春分']
{"type": "timestamp", "timestamp": "2019-03-21 00:00:00"}
====
目标字符串:  7000万
基础时间 2019-7-28-15-47-27
temp ['70000000']
{"type": "error", "error": "no time pattern could be extracted."}
====
目标字符串:  7百
基础时间 2019-7-28-15-47-27
temp []
{"type": "error", "error": "no time pattern could be extracted."}
====
目标字符串:  7千
基础时间 2019-7-28-15-47-27
temp []
{"type": "error", "error": "no time pattern could be extracted."}
====
```

## 使用方式 

见 `Test.py`

## TODO

| 问题                  | 现在版本                                       | 正确                                            |
| --------------------- | ---------------------------------------------- | ----------------------------------------------- |
| 晚上8点到上午10点之间 | ["2018-03-16 20:00:00", "2018-03-16 22:00:00"] | ["2018-03-16 20:00:00", "2018-03-17 10:00:00"]" |

## 声明

为了适合自己的编程习惯，删除了代码中部分文件的头部注释信息，信息格式如下，特此声明：

```python
# -*- coding: utf-8 -*-
# @Time    : xxxxxxxx
# @Author  : zhm
# @File    : xxxxx
# @Software: PyCharm
# @Changed : tianyuningmou
```
