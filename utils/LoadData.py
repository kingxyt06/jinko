import json
import os

import requests
import yaml

from utils.YamlUtil import YamlUtil


def load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    # standard_yaml(data)
    # 因为读取的yaml数据是列表，需要转化为dict，但这又是个不规则的列表里面嵌着字典，所以需要特殊处理
    # for data_item in data:
    #     data_keys = data_item.keys()
    #     print(f"数据项的键：{data_keys}")
    #
    # if 'name' in data_keys and 'request' in data_keys and 'validate' in data_keys:
    #     request_keys = data_item['request'].keys()
    #     req_kwargs = data_item['request']
    #     if 'method' in request_keys and 'url' in request_keys:
    #         print("yaml基础结构检查正确")
    #         method = req_kwargs.pop('method')
    #         url = req_kwargs.pop('url')
    #         # 处理请求参数
    #         for key, value in req_kwargs.items():
    #             if key in ['params', 'data', 'json', 'headers', 'cookies']:
    #                 req_kwargs[key] = replace_value(value)


def send_request(method, url, **kwargs):
    method = str(method).lower()  # 转换小写
    # 基础路径的拼接和替换
    url = "https://jinkoscf-agw-qa.llsstd.com/" + url
    for key, value in kwargs.items():
        if key in ['params', 'data', 'json', 'headers', 'cookies']:
            kwargs[key] = replace_value(value)
    print(kwargs)
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
                print(f"替换成功",str_data)
        # if isinstance(str_data, dict) or isinstance(str_data, list):
        #     data = json.loads(str_data)
        if isinstance(str_data, str):
            data = json.loads(str_data)
        return data


if __name__ == '__main__':
    # relative_path = "../extract.yaml"
    # print(os.getcwd())
    # # print(os.path.abspath(os.getcwd()))
    # print(os.path.join(os.getcwd(),relative_path))

    current_dir = os.getcwd()

    print(os.path.dirname(current_dir))
    print(os.path.join(os.path.dirname(current_dir), "extract.yaml"))

    # res = YamlUtil().read_data('/test_data/user-web/CheckCode.yaml')
    # print(type(res))
    # load('../test_data/user-web/login_agw.yaml')
