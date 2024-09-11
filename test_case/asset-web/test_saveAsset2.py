import json

import pytest
import yaml

from utils import LoadData

import os

from utils.YamlUtil import YamlReader

print(os.getcwd())


class TestSaveAsset:
    @pytest.mark.parametrize('args', YamlReader().read_data('/test_data/asset-web/Asset.yaml'))
    def test_saveAsset(self, args, get_agw_token, req_AGW):
        print(f"加载的参数：{args}")
        cookies = get_agw_token
        r = req_AGW
        url = 'asset-web/asset/saveAsset'
        res = r.visit(method='POST',
                      url=url,
                      cookies=cookies,
                      json=args,
                      )
        print(f"请求的 body：{res.request.body}")
        print(f"服务器响应内容：{res.text}")
        res = json.loads(res.text)
        assert res['data'] == True


