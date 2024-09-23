import os.path

import yaml


class YamlUtil:
    def __init__(self):
        self._data = None
        self._data_all = None


    def load_data(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        if not self._data:
            with open(self.yamlf, "rb") as f:
                self._data = yaml.safe_load(f)
                return self._data

    def data_all(self):
        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all = yaml.safe_load_all(f)
                return self._data_all

    # 读取
    def read_yaml(self, key):
        # print(os.getcwd())
        with open(os.path.join(os.path.dirname(os.getcwd()), "extract.yaml"), encoding='utf-8', mode='r') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key]

    # 写入
    def write_yaml(self, data):
        with open(os.path.join(os.path.dirname(os.getcwd()), "extract.yaml"), encoding='utf-8', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清空
    def clear_yaml(self):
        with open(os.path.join(os.path.dirname(os.getcwd()), "extract.yaml"), encoding='utf-8', mode='w') as f:
            f.truncate()

    # 加载数据
    def read_data(self, yaml_name):
        current_path = os.path.abspath(__file__)
        BASE_DIR = os.path.dirname(os.path.dirname(current_path))
        with open(BASE_DIR + yaml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value

    # 读取测试用例
    def read_testcase(self, yaml_name):
        print(os.getcwd() + "\\" + yaml_name)
        with open(os.getcwd() + "\\" + yaml_name, encoding='utf-8') as f:
            value = yaml.load(f, yaml.FullLoader)
            return value
