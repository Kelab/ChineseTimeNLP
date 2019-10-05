from time_converter import TimeNormalizer  # 引入包
from time_converter.log import Time_NLP_LOGGER
Time_NLP_LOGGER.setLevel(10)
tn = TimeNormalizer(isPreferFuture=False)

res = tn.parse(target=u'下周五我有什么课')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'星期日我有什么课')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'八月十五号晚上我有什么课')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'晚上8点到上午10点之间')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(
    target=u'2013年二月二十八日下午四点三十分二十九秒',
    timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(
    target=u'我需要大概33天2分钟四秒',
    timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'今年儿童节晚上九点一刻')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'三日')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'7点4')  # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
print('====\n')

res = tn.parse(target=u'2个小时以前')
print(res)
print('====\n')

res = tn.parse(target=u'三日后')
print(res)
print('====\n')
res = tn.parse(target=u'三天后')
print(res)
print('====\n')
