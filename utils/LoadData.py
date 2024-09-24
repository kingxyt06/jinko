import json
import os

import requests
import yaml

from utils.YamlUtil import YamlUtil


def send_request(method, url, **kwargs):
    method = str(method).lower()  # 转换小写
    # 基础路径的拼接和替换
    url = "https://jinkoscf-agw-qa.llsstd.com/" + url
    for key, value in kwargs.items():
        if key in ['params', 'data', 'json', 'headers', 'cookies']:
            kwargs[key] = replace_value(value)
    res = requests.session().request(method, url, **kwargs)
    print(res.request.body)
    return res


def standard_yaml(caseinfo):
    caseinfo_keys = caseinfo.keys()
    print(caseinfo_keys)
    if 'name' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
        request_keys = caseinfo['request'].keys()
        if 'method' and 'url' in request_keys:
            print("yaml基础结构检查正确")
            method = caseinfo['request'].pop('method')
            url = caseinfo['request'].pop('url')
            res = send_request(method, url, **caseinfo['request'])
            return res


def replace_value(data):
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


def read_testcase(yaml_name):
    with open(os.path.dirname(os.getcwd()) + '\\test_data\\' + yaml_name, mode='r', encoding='utf-8') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)

        return caseinfo


def read_datas(yaml_name):
    with open(os.path.dirname(os.getcwd()) + '\\datas\\' + yaml_name, mode='r', encoding='utf-8') as f:
        datas = yaml.load(f, yaml.FullLoader)
        if len(datas)>=2:
            return datas



if __name__ == '__main__':
    # relative_path = "../extract.yaml"
    # print(os.getcwd())
    # # print(os.path.abspath(os.getcwd()))
    # print(os.path.join(os.getcwd(),relative_path))

    # current_dir = os.getcwd()
    #
    # print(os.path.dirname(current_dir))
    # print(os.path.join(os.path.dirname(current_dir), "extract.yaml"))
    datas = read_datas('limit-web\creditEffect_limit_data.yaml')
    print(datas)

    res = read_testcase('limit-web\creditEfectLimit.yaml')
    # print(res[0]['parameterize'])  # {'name-cookies-current-size-queryCondition-assert_str': '/datas/creditEffect_limit_data.yaml'}

    param_list = []
    for k, v in res[0]['parameterize'].items():
        #param_list = ['name', 'cookies', 'current', 'size', 'queryCondition', 'assert_str']
        param_list = k.split("-")
        datas_list = read_datas('limit-web\creditEffect_limit_data.yaml')
        length_flag = True
        for data in datas_list:
            if len(data) != len(param_list):
                length_flag = False
                break

        new_caseinfo = []
        if length_flag:
            for x in range(1, len(datas_list)):
                print(datas_list[x])
                for y in range(0, len(datas_list[x])):
                    print(datas_list[0][y])
                    if datas_list[0][y] in param_list:



