
import pytest

from utils.LoadData import read_testcase
from utils.RequestUtil import RequestUtill
from utils.YamlUtil import YamlUtil


class TestLimit:

    @pytest.mark.parametrize('caseinfo', read_testcase('limit-web/creditEfectLimit.yaml'))
    def test_creditEfectLimitPage(self, caseinfo):
        # print(caseinfo['parameterize'])

        res = RequestUtill().standard_yaml(caseinfo)
        print(res.request.body)



