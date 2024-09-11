import json

import requests
import yaml


def load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    # 因为读取的yaml数据是列表，需要转化为dict，但这又是个不规则的列表里面嵌着字典，所以需要特殊处理
    for data_item in data:
        data_keys = data_item.keys()
        print(f"数据项的键：{data_keys}")

    if 'name' in data_keys and 'request' in data_keys and 'validate' in data_keys:
        request_keys = data_item['request'].keys()
        if 'method' in request_keys and 'url' in request_keys:
            print("yaml基础结构检查正确")
            method = data_item['request'].pop('method')
            url = data_item['request'].pop('url')
            # 处理请求参数
            for key, value in data_item['request'].items():
                if key in ['params', 'data', 'json', 'headers']:
                    data_item['request'][key] = replace_value(value)


def replace_value(data):
    print(type(data))
    if isinstance(data, dict) or isinstance(data, list):
        str_data = json.dumps(data)
    else:
        str_data = str(data)
        print(str_data)
    # for cs in range(str_data.count('${')):
    #     if '${' in str_data and "}" in str_data:
    #
    return str_data


if __name__ == '__main__':
    # cookies = {'cookies':""}
    # res = requests.Session().request(method,
    #               url,
    #               cookies=cookies,
    #               **data_item['request'],
    #               )
    # print(res)
    load('../test_data/asset-web/saveAsset.yaml')
