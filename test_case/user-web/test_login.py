import json
import re
import time

import pytest
import requests
from redis import Redis
from config.conf import ConfigReader
from utils.LoadData import replace_value
from utils.RedisUtil import RedisUtill
from utils.YamlUtil import YamlUtil


class TestLogin:
    @pytest.mark.parametrize('args', YamlUtil().read_data('/test_data/user-web/CheckCode.yaml'))
    def test_getcode(self, args):
        method = args['request'].pop('method')
        url = args['request'].pop('url')
        args['request']['params'] = {'timestamp': int(round(time.time() * 1000))}

        res = requests.session().request(method=method,
                                         url="https://jinkoscf-agw-qa.llsstd.com/" + url,
                                         params=args['request']['params'])
        picCheckCodeKey = res.cookies.get_dict()['CAPTCHAID']
        rdsV = RedisUtill().rds_get(picCheckCodeKey)
        picCheckCode = re.sub(r'"', '', rdsV)
        print("登陆验证码为 : " + picCheckCode)

        if "extract" in args.keys():
            for key, value in args["extract"].items():
                values = {'picCheckCodeKey': picCheckCodeKey, 'picCheckCode': picCheckCode}
                if "(.*?)" in value or "(.+?)" in value:
                    if key in values:
                        extract_value = {key: values[key]}
                        YamlUtil().write_yaml(extract_value)

    @pytest.mark.parametrize('args', YamlUtil().read_data('/test_data/user-web/login_agw.yaml'))
    def test_login(self, args):
        method = args['request'].pop('method')
        url = args['request'].pop('url')
        data = replace_value(args['request'])
        # if isinstance(args['request'], dict):
        #     str_data = json.dumps(args['request'])
        #     for i in range(1, str_data.count("${") + 1):
        #         if '${' and '}' in str_data:
        #             start_index = str_data.index("${")
        #             end_index = str_data.index("}", start_index)
        #             old_value = str_data[start_index:end_index + 1]
        #             new_value = YamlUtil().read_yaml(old_value[2:-1])
        #             str_data = str_data.replace(old_value, new_value)
        #     if isinstance(str_data, str):
        #         data = json.loads(str_data)

        res = requests.session().request(method=method, url="https://jinkoscf-agw-qa.llsstd.com/" + url
                                         , json=data['json'], cookies=data['cookies'])
        cookies_sub = []
        cookies_dict = requests.utils.dict_from_cookiejar(res.cookies)
        for key, value in cookies_dict.items():
            cookies_sub.append({key: value})

        if "extract" in args.keys():
            for key, value in args["extract"].items():
                for k, v in value.items():
                    for ck in cookies_sub:
                        if k in ck:
                            args["extract"][key][k] = ck[k]
        YamlUtil().write_yaml(args["extract"])
