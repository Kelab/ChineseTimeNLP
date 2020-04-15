import regex as re


# * 字符串预处理模块，为分析器TimeNormalizer提供相应的字符串预处理服务
class StringPreHandler:
    @classmethod
    def delKeyword(cls, target, rules):
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

    @classmethod
    def numberTranslator(cls, target):
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
        pattern = re.compile(u"[一二两三四五六七八九123456789]万[一二两三四五六七八九123456789](?!(千|百|十))")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"万")
            s = list(filter(None, s))
            num = 0
            if len(s) == 2:
                num += cls.wordToNumber(s[0]) * 10000 + cls.wordToNumber(s[1]) * 1000
            target = pattern.sub(str(num), target, 1)

        pattern = re.compile(u"[一二两三四五六七八九123456789]千[一二两三四五六七八九123456789](?!(百|十))")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"千")
            s = list(filter(None, s))
            num = 0
            if len(s) == 2:
                num += cls.wordToNumber(s[0]) * 1000 + cls.wordToNumber(s[1]) * 100
            target = pattern.sub(str(num), target, 1)

        pattern = re.compile(u"[一二两三四五六七八九123456789]百[一二两三四五六七八九123456789](?!十)")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"百")
            s = list(filter(None, s))
            num = 0
            if len(s) == 2:
                num += cls.wordToNumber(s[0]) * 100 + cls.wordToNumber(s[1]) * 10
            target = pattern.sub(str(num), target, 1)

        pattern = re.compile(u"[零一二两三四五六七八九]")
        match = pattern.finditer(target)
        for m in match:
            target = pattern.sub(str(cls.wordToNumber(m.group())), target, 1)

        # 星期天表达式替换为星期7
        pattern = re.compile(u"(?<=(周|星期))[末天日]")
        match = pattern.finditer(target)
        for m in match:
            target = pattern.sub("7", target, 1)

        pattern = re.compile(u"(?<!(周|星期))0?[0-9]?十[0-9]?")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"十")
            num = 0
            ten = cls.strToInt(s[0])
            if ten == 0:
                ten = 1
            unit = cls.strToInt(s[1])
            num = ten * 10 + unit
            target = pattern.sub(str(num), target, 1)

        pattern = re.compile(u"0?[1-9]百[0-9]?[0-9]?")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"百")
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

        pattern = re.compile(u"0?[1-9]千[0-9]?[0-9]?[0-9]?")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"千")
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

        pattern = re.compile(u"[0-9]+万[0-9]?[0-9]?[0-9]?[0-9]?")
        match = pattern.finditer(target)
        for m in match:
            group = m.group()
            s = group.split(u"万")
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

        return target

    @classmethod
    def wordToNumber(cls, s):
        """
        方法numberTranslator的辅助方法，可将[零-九]正确翻译为[0-9]
        :param s: 大写数字
        :return: 对应的整形数，如果不是数字返回-1
        """
        return {
            "零": 0,
            "0": 0,
            "一": 1,
            "1": 1,
            "二": 2,
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

    @classmethod
    def strToInt(cls, s: str):
        try:
            res = int(s)
        except Exception:
            res = 0
        return res
