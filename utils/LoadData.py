import json
import os
import re

import requests
import yaml

from utils.YamlUtil import YamlUtil


def send_request(method, url, **kwargs):
    method = str(method).lower()  # 转换小写
    # 基础路径的拼接和替换
    url = "https://jinkoscf-agw-qa.llsstd.com/" + url
    for key, value in kwargs.items():
        if key in ['params', 'data', 'json', 'headers', 'cookies']:
            # print(type(value))
            # 进行变量替换
            kwargs[key] = replace_value(value)
    # print(kwargs[key])
    res = requests.session().request(method, url, **kwargs)
    # print(res.request.body)
    return res



def process_query_condition(value):
    if isinstance(value, str) and re.match(r'^[\'\"]{.*}[\'\"]$', value):
        try:
            cleaned_value = value[1:-1]
            json_dict = json.loads(cleaned_value.replace("'", '"'))
            if isinstance(json_dict, dict):
                return json_dict
            else:
                return value
        except json.JSONDecodeError:
            return value
    else:
        return value



def standard_yaml(caseinfo):
    # print(caseinfo)
    caseinfo_keys = caseinfo.keys()
    # print(caseinfo_keys)
    if 'name' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
        request_keys = caseinfo['request'].keys()
        if 'method' and 'url' in request_keys:
            print("yaml基础结构检查正确")
            method = caseinfo['request'].pop('method')
            url = caseinfo['request'].pop('url')
            # 处理参数存在'{}'带引号的问题，发起请求返回值出现:数据格式不正确
            # 如果请求的传参的值用{}包起来，那就要在发起请求前，做一次去除双引号的处理..例：'json': {'queryCondition': '{}'} ===> 'json': {'queryCondition': {}}
            if 'json' in caseinfo['request']:
                json_data = caseinfo['request']['json']

                for key, value in json_data.items():
                    if isinstance(value, str) and re.match(r'^\{.*\}$', value):
                        try:
                            json_data[key] = json.loads(value)
                        except json.JSONDecodeError:
                            pass
            print(caseinfo['request']['json'])
            res = send_request(method, url, **caseinfo['request'])
            return res


def replace_value(data):
    # print(data)
    if data:
        # 保存数据类型
        data_type = type(data)
        if isinstance(data, dict) or isinstance(data, list):
            str_data = json.dumps(data, ensure_ascii=False)
        else:
            str_data = str(data)

        for cs in range(1, str_data.count('${') + 1):
            if '${' in str_data and '}' in str_data:
                start_index = str_data.index('${')
                end_index = str_data.index('}', start_index)
                old_value = str_data[start_index:end_index + 1]
                new_value = YamlUtil().read_yaml(old_value[2:-1])
                # print(new_value)
                str_data = str_data.replace(old_value, str(new_value))
                if old_value == '${cookies}':
                    str_data = str_data.replace("'", '"')
                # print(f"替换成功", str_data)

        if isinstance(str_data, str) and str_data.find('CURRENT-LOGIN') != -1:
            data = json.loads(str_data)
        elif isinstance(str_data, dict) or isinstance(str_data, list):
            data = data_type(str_data)
        else:
            data = json.loads(str_data)
    return data



def process_json_value(value):
    if isinstance(value, str):
        # 匹配单引号或双引号包裹的类似 JSON 的字符串
        pattern = r'^[\'"].*[\'"]$'
        if re.match(pattern, value):
            try:
                # 去除首尾引号后尝试解析为 JSON 对象
                cleaned_value = value[1:-1]
                return json.loads(cleaned_value.replace("'", '"'))
            except json.JSONDecodeError:
                return value
    else:
        return value

def read_testcase(yaml_name):
    with open(os.path.dirname(os.getcwd()) + '\\test_case\\' + yaml_name, mode='r', encoding='utf-8') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)
        if len(caseinfo) >= 2:
            return caseinfo
        else:
            if "parameterize" in dict(*caseinfo).keys():
                new_caseinfo = ddt(*caseinfo)
                return new_caseinfo
            else:
                return caseinfo


def read_datas(yaml_name):
    with open(os.path.dirname(os.getcwd()) + '\\datas\\' + yaml_name, mode='r', encoding='utf-8') as f:
        datas = yaml.load(f, yaml.FullLoader)
        if len(datas) >= 2:
            return datas


def ddt(caseinfo):
    if 'parameterize' in caseinfo.keys():
        # print(type(caseinfo))
        caseinfo_str = json.dumps(caseinfo)
        # print(type(caseinfo_str))
        for param_key, param_value in caseinfo['parameterize'].items():
            # param_list = ['name', 'cookies', 'current', 'size', 'queryCondition', 'assert_str']
            param_list = param_key.split("-")
            datas_list = read_datas(param_value)
            length_flag = True
            for data in datas_list:
                if len(data) != len(param_list):
                    length_flag = False
                    break

            new_caseinfo = []
            if length_flag:
                for x in range(1, len(datas_list)):
                    # print(datas_list[x])
                    temp_caseinfo = caseinfo_str
                    for y in range(0, len(datas_list[x])):
                        # print(datas_list[0][y])
                        if datas_list[0][y] in param_list:
                            if isinstance(datas_list[x][y], int) or isinstance(datas_list[x][y], float):
                                temp_caseinfo = temp_caseinfo.replace('"$ddt{' + datas_list[0][y] + '}"',
                                                                      str(datas_list[x][y]))
                            else:
                                temp_caseinfo = temp_caseinfo.replace("$ddt{" + datas_list[0][y] + "}",
                                                                      str(datas_list[x][y]))
                    new_caseinfo.append(json.loads(temp_caseinfo))
        return new_caseinfo
    else:
        return caseinfo


if __name__ == '__main__':
    # relative_path = "../extract.yaml"
    # print(os.getcwd())
    # # print(os.path.abspath(os.getcwd()))
    # print(os.path.join(os.getcwd(),relative_path))

    # current_dir = os.getcwd()
    #
    # print(os.path.dirname(current_dir))
    # print(os.path.join(os.path.dirname(current_dir), "extract.yaml"))
    # datas = read_datas('limit-web\creditEffect_limit_data.yaml')
    # print(datas)

    caseinfo = read_testcase('limit-web\creditEfectLimit.yaml')
    # print(len(caseinfo))
    for x in range(0, len(caseinfo)):
        # print(caseinfo[x])
        res = standard_yaml(caseinfo[x])
        # print(res.request.body)
        print(res.text)
