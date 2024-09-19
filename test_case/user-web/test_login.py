import re
import time

import pytest
import requests

from utils.LoadData import replace_value, standard_yaml, send_request
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
                if key in values:
                    extract_value = {key: values[key]}
                    YamlUtil().write_yaml(extract_value)

    # @pytest.mark.parametrize('args', YamlUtil().read_data('/test_data/user-web/login_agw.yaml'))
    # def test_login(self, args):
    #     method = args['request'].pop('method')
    #     url = args['request'].pop('url')
    #     data = replace_value(args['request'])
    #
    #     res = requests.session().request(method=method, url="https://jinkoscf-agw-qa.llsstd.com/" + url
    #                                      , json=data['json'], cookies=data['cookies'])
    #     cookies_sub = []
    #     cookies_dict = requests.utils.dict_from_cookiejar(res.cookies)
    #     for key, value in cookies_dict.items():
    #         cookies_sub.append({key: value})
    #
    #     if "extract" in args.keys():
    #         for key, value in args["extract"].items():
    #             for k, v in value.items():
    #                 for ck in cookies_sub:
    #                     if k in ck:
    #                         args["extract"][key][k] = ck[k]
    #     YamlUtil().write_yaml(args["extract"])

    @pytest.mark.parametrize('args', YamlUtil().read_data('/test_data/user-web/login_agw.yaml'))
    def test_login(self,args):
        res = standard_yaml(args)

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