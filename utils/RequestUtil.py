import json
import requests
from config.conf import ConfigReader
from utils.YamlUtil import YamlUtil


class RequestUtill:

    def __init__(self, url_type="agw"):
        self.url_type = url_type

        if self.url_type == "agw":
            self.base_url = ConfigReader().get_conf_agw_url()
            print("\n当前内管端域名:" + self.base_url)
        else:
            self.base_url = ConfigReader().get_conf_sp_url()
            print("当前客户端域名:" + self.base_url)
        self.session = requests.session()

    def standard_yaml(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        # print(caseinfo_keys)
        if 'name' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
            request_keys = caseinfo['request'].keys()
            if 'method' and 'url' in request_keys:
                print("yaml基础结构检查正确")
                method = caseinfo['request'].pop('method')
                url = caseinfo['request'].pop('url')
                res = self.send_request(method, url, **caseinfo['request'])
                return_code = res.status_code
                res_json = res.json()
                self.assert_result(caseinfo['validate'], return_code, res_json)
                return res

    def send_request(self, method, url, **kwargs):
        method = str(method).lower()  # 转换小写
        # 基础路径的拼接和替换
        url = self.base_url + url
        for key, value in kwargs.items():
            if key in ['params', 'data', 'json', 'headers', 'cookies']:
                kwargs[key] = self.replace_value(value)
        res = self.session.request(method, url, **kwargs)
        return res

    def replace_value(self, data):
        # print(type(data))
        if data:
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)

            for cs in range(1, str_data.count('${') + 1):
                if '${' in str_data and '}' in str_data:
                    start_index = str_data.index('${')
                    end_index = str_data.index('}', start_index)
                    old_value = str_data[start_index:end_index + 1]
                    new_value = YamlUtil().read_yaml(old_value[2:-1])
                    str_data = str_data.replace(old_value, str(new_value))
                    print(f"替换成功", str_data)
            # if isinstance(str_data, dict) or isinstance(str_data, list):
            #     data = json.loads(str_data)
            if isinstance(str_data, str):
                data = json.loads(str_data)
            return data

    def assert_result(self, yq_result, return_code, res_json):
        all_flag = 0
        for yq in yq_result:
            for key, value in yq.items():
                if key == "equals":
                    flag = self.equals_assert(value, return_code)
                    all_flag = all_flag + flag
                elif key == "contains":
                    flag = self.contains_assert(value, res_json)
                    all_flag = all_flag + flag
                else:
                    print("框架暂不支持此段断言方式")
        assert all_flag == 0

    def equals_assert(self, value, return_code):
        flag = 0
        for assert_key, assert_val in value.items():
            if assert_key == 'code':
                assert_val == return_code
                print(f"断言正确,{assert_key}为{return_code}")
                if assert_val != return_code:
                    flag = flag + 1
                    print("断言失败，返回的状态码不等于%s" % assert_val)
        return flag

    def contains_assert(self, value, return_json):
        flag = 0
        if str(value) not in str(return_json):
            flag = flag + 1
            print("断言失败：返回的结果中不包含：" + str(value))
        print(f"断言正确,{value}包含在{return_json}")
        return flag
