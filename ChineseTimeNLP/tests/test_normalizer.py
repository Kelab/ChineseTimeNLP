from ..normalizer import TimeNormalizer


class TestNormalizer:
    tn = TimeNormalizer(isPreferFuture=False)

    def test_year(self):
        res = self.tn.parse(target=u"0.5小时后")
        assert res["type"] == "timedelta"
        assert res[res["type"]]["hour"] == 5
