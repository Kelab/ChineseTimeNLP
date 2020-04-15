import regex as re
from loguru import logger


def filter_irregular_expression(input_query):
    logger.debug(f"对一些不规范的表达：转换前 {input_query}")

    # 这里对于下个周末这种做转化 把个给移除掉
    input_query = number_translator(input_query)

    rule = r"[0-9]月[0-9]"
    pattern = re.compile(rule)
    match = pattern.search(input_query)
    if match is not None:
        index = input_query.find("月")
        rule = r"日|号"
        pattern = re.compile(rule)
        match = pattern.search(input_query[index:])
        if match is None:
            rule = r"[0-9]月[0-9]+"
            pattern = re.compile(rule)
            match = pattern.search(input_query)
            if match is not None:
                end = match.span()[1]
                input_query = input_query[:end] + "号" + input_query[end:]
    # 一个半小时
    pattern = re.compile(r"(.*半)(?=(小时|月))")
    match = pattern.search(input_query)
    if match is not None:
        test_ge = re.compile(r"(.*)(?=个半)")
        test_ge_match = test_ge.match(match.group())
        if match.group() == "半":
            input_query = input_query.replace("半", "0.5")
        elif test_ge_match is not None:
            number = test_ge_match.group() + ".5"
            input_query = input_query.replace(test_ge_match.group() + "个半", number)

    pattern = re.compile(r"小时|月")
    match = pattern.search(input_query)
    if match is None:
        input_query = input_query.replace("个", "")

    input_query = input_query.replace("中旬", "15号")
    input_query = input_query.replace("傍晚", "午后")
    input_query = input_query.replace("大年", "")
    input_query = input_query.replace("新年", "春节")
    input_query = input_query.replace("五一", "劳动节")
    input_query = input_query.replace("白天", "早上")
    input_query = input_query.replace("：", ":")
    logger.debug(f"对一些不规范的表达：转换后 {input_query}")
    return input_query


def del_keyword(target, rules):
    """
    该方法删除一字符串中所有匹配某一规则字串
    可用于清理一个字符串中的空白符和语气助词
    :param target: 待处理字符串
    :param rules: 删除规则
    :return: 清理工作完成后的字符串
    """
    pattern = re.compile(rules)
    res = pattern.sub("", target)
    return res


def number_translator(target):
    """
    该方法可以将字符串中所有的用汉字表示的数字转化为用阿拉伯数字表示的数字
    如"这里有一千两百个人，六百零五个来自中国"可以转化为
    "这里有1200个人，605个来自中国"
    此外添加支持了部分不规则表达方法
    如两万零六百五可转化为20650
    两百一十四和两百十四都可以转化为214
    一六零加一五八可以转化为160+158
    该方法目前支持的正确转化范围是0-99999999
    该功能模块具有良好的复用性
    :param target: 待转化的字符串
    :return: 转化完毕后的字符串
    """
    logger.debug(f"before number_translator: {target}")
    pattern = re.compile(r"[一二两三四五六七八九123456789]万[一二两三四五六七八九123456789](?!(千|百|十))")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("万")
        s = list(filter(None, s))
        num = 0
        if len(s) == 2:
            num += word2number(s[0]) * 10000 + word2number(s[1]) * 1000
        target = pattern.sub(str(num), target, 1)

    pattern = re.compile(r"[一二两三四五六七八九123456789]千[一二两三四五六七八九123456789](?!(百|十))")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("千")
        s = list(filter(None, s))
        num = 0
        if len(s) == 2:
            num += word2number(s[0]) * 1000 + word2number(s[1]) * 100
        target = pattern.sub(str(num), target, 1)

    pattern = re.compile(r"[一二两三四五六七八九123456789]百[一二两三四五六七八九123456789](?!十)")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("百")
        s = list(filter(None, s))
        num = 0
        if len(s) == 2:
            num += word2number(s[0]) * 100 + word2number(s[1]) * 10
        target = pattern.sub(str(num), target, 1)

    pattern = re.compile(r"[零一二两三四五六七八九]")
    match = pattern.finditer(target)
    for m in match:
        target = pattern.sub(str(word2number(m.group())), target, 1)

    # 星期天表达式替换为星期7
    pattern = re.compile("(?<=(周|星期))[末天日]")
    match = pattern.finditer(target)
    for m in match:
        target = pattern.sub("7", target, 1)

    pattern = re.compile("(?<!(周|星期))0?[0-9]?十[0-9]?")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("十")
        num = 0
        ten = str2int(s[0])
        if ten == 0:
            ten = 1
        unit = str2int(s[1])
        num = ten * 10 + unit
        target = pattern.sub(str(num), target, 1)

    pattern = re.compile("0?[1-9]百[0-9]?[0-9]?")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("百")
        s = list(filter(None, s))
        num = 0
        if len(s) == 1:
            hundred = int(s[0])
            num += hundred * 100
        elif len(s) == 2:
            hundred = int(s[0])
            num += hundred * 100
            num += int(s[1])
        target = pattern.sub(str(num), target, 1)

    pattern = re.compile("0?[1-9]千[0-9]?[0-9]?[0-9]?")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("千")
        s = list(filter(None, s))
        num = 0
        if len(s) == 1:
            thousand = int(s[0])
            num += thousand * 1000
        elif len(s) == 2:
            thousand = int(s[0])
            num += thousand * 1000
            num += int(s[1])
        target = pattern.sub(str(num), target, 1)

    pattern = re.compile("[0-9]+万[0-9]?[0-9]?[0-9]?[0-9]?")
    match = pattern.finditer(target)
    for m in match:
        group = m.group()
        s = group.split("万")
        s = list(filter(None, s))
        num = 0
        if len(s) == 1:
            tenthousand = int(s[0])
            num += tenthousand * 10000
        elif len(s) == 2:
            tenthousand = int(s[0])
            num += tenthousand * 10000
            num += int(s[1])
        target = pattern.sub(str(num), target, 1)

    logger.debug(f"after number_translator: {target}")
    return target


def word2number(s: str):
    """
    方法number_translator的辅助方法，可将[零-九]正确翻译为[0-9]
    :param s: 大写数字
    :return: 对应的整形数，如果不是数字返回-1
    """
    return {
        "零": 0,
        "0": 0,
        "一": 1,
        "1": 1,
        "二": 2,
        "两": 2,
        "2": 2,
        "三": 3,
        "3": 3,
        "四": 4,
        "4": 4,
        "五": 5,
        "5": 5,
        "六": 6,
        "6": 6,
        "七": 7,
        "7": 7,
        "八": 8,
        "8": 8,
        "九": 9,
        "9": 9,
    }.get(s, -1)


def str2int(s: str):
    try:
        res = int(s)
    except Exception:
        res = 0
    return res
