import re
import time

import pytest
import requests
from redis import Redis
from config.conf import ConfigReader
from utils.YamlUtil import YamlUtil


class TestLogin:
    @pytest.mark.parametrize('args', YamlUtil().read_data('/test_data/user-web/CheckCode.yaml'))
    def test_getcode(self, args):
        redis_url = ConfigReader().get_conf_redis()
        redis_db = ConfigReader().get_redis_db()
        rds = Redis(host=redis_url, port='6379', password='', decode_responses=True, db=redis_db)
        print(args)
        method = args['request'].pop('method')
        url = args['request'].pop('url')
        args['request']['params'] = {'timestamp': int(round(time.time() * 1000))}

        res = requests.session().request(method=method, url="https://jinkoscf-agw-qa.llsstd.com/" + url,
                                         params=args['request']['params'])
        picCheckCodeKey = res.cookies.get_dict()['CAPTCHAID']
        rdsV = rds.get(picCheckCodeKey)
        picCheckCode = re.sub(r'"', '', rdsV)
        print("登陆验证码为 : " + picCheckCode)
        # YamlUtil().write_yaml({'picCheckCode':picCheckCode})
        if "extract" in args.keys():
            for key, value in args["extract"].items():
                if "(.*?)" in value or "(.+?)" in value:
                    zz_value = re.search(value,res.cookies.get_dict())
                    print(zz_value)






    def test_login(self):
        pass
