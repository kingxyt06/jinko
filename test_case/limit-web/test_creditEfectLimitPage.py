import pytest

from utils.LoadData import standard_yaml
from utils.YamlUtil import YamlUtil


class TestLimit:

    @pytest.mark.parametrize('args', YamlUtil().read_data('/test_data/limit-web/creditEfectLimit.yaml'))
    def test_creditEfectLimitPage(self, args):
        res = standard_yaml(args)
        print(res.text)
