from ..normalizer import TimeNormalizer


class TestNormalizer:
    tn = TimeNormalizer(isPreferFuture=False)

    def test_case1(self):
        res = self.tn.parse(target="我需要大概33天2分钟四秒")
        assert res["type"] == "timedelta"
        assert res[res["type"]]["year"] == 0
        assert res[res["type"]]["month"] == 0
        assert res[res["type"]]["day"] == 33
        assert res[res["type"]]["hour"] == 0
        assert res[res["type"]]["minute"] == 2
        assert res[res["type"]]["second"] == 4

    def test_case2(self):
        res = self.tn.parse(target="2013年二月二十八日下午四点三十分二十九秒")
        assert res["type"] == "timestamp"
        assert res[res["type"]] == "2013-02-28 16:30:29"

    def test_case3(self):
        res = self.tn.parse(target="今年儿童节晚上九点一刻", baseTime="2021-07-01")
        assert res["type"] == "timestamp"
        assert res[res["type"]] == "2021-06-01 21:15:00"

    def test_case4(self):
        res = self.tn.parse(target="本月三日", baseTime="2021-07-01")
        assert res["type"] == "timestamp"
        assert res[res["type"]] == "2021-07-03 00:00:00"

    def test_case5(self):
        res = self.tn.parse(target="7点4分", baseTime="2021-07-01")
        assert res["type"] == "timestamp"
        assert res[res["type"]] == "2021-07-01 07:04:00"
