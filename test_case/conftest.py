import json
import os
import re
import time
import pytest
from redis import Redis

from config.conf import ConfigReader

# from utils.Encryption import get_publicKey, Encryption
from utils.MysqlUtil import MySQLClient
from utils.ObjectPool import ObjectPool
from utils.RequestsUtil import RequestsUtil
from utils.YamlUtil import YamlReader


@pytest.fixture(scope="session", autouse=True)
def init_pools():
    sqlConf = ConfigReader().get_conf_SqlMessage()
    pools = ObjectPool()
    # 实例化两个类，并放进去
    req_agw = RequestsUtil(url_type="agw")
    req_sp = RequestsUtil(url_type="sp")
    c = ConfigReader()
    # sqlU = MySQLClient(host=sqlConf['mysql-url'],
    #                    port=5470,
    #                    user="root",
    #                    password="123456"
    #                    )
    pools.add_object({'reqA': req_agw})
    pools.add_object({'reqS': req_sp})
    pools.add_object({'confU': c})
    # pools.add_object({'sqlU': sqlU})
    print(f"------------初始化对象池啦-----------:\n{pools.pool}")
    return pools



@pytest.fixture(scope="session", autouse=True)
def req_AGW(init_pools):
    return init_pools.get_object('reqA')


@pytest.fixture(scope="session", autouse=True)
def req_SP(init_pools):
    return init_pools.get_object('reqS')


@pytest.fixture(scope="session", autouse=True)
def conf_utill(init_pools):
    return init_pools.get_object('confU')


@pytest.fixture(scope="session", autouse=True)
def sql_utill(init_pools):
    return init_pools.get_object('sqlU')




@pytest.fixture(scope="session", autouse=True)
def get_agw_token(init_pools, req_AGW, conf_utill):
    print("\n前置步骤----获取内管端cookie")
    global token
    redis_url = conf_utill.get_conf_redis()
    redis_db = conf_utill.get_redis_db()
    rds = Redis(host=redis_url, port='6379', password='', decode_responses=True, db=redis_db)
    captcha_data = {'timestamp': int(round(time.time() * 1000))}
    url = "tools-web/captcha/code/get"
    res = req_AGW.visit(method="GET", url=url, params=captcha_data)
    picCheckCodeKey = res.cookies.get_dict()['CAPTCHAID']

    rdsV = rds.get(picCheckCodeKey)
    picCheckCode = re.sub(r'"', '', rdsV)

    print("登陆验证码为 : " + picCheckCode)
    username = conf_utill.get_agw_username()
    password = conf_utill.get_agw_pwd()
    login_params = {
        "password": password,
        "picCheckCode": picCheckCode,
        "userName": username
    }
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '0'}
    cookies = {'CAPTCHAID': picCheckCodeKey}
    login_url = "user-web/user/login"
    login_res = req_AGW.visit(method="POST", url=login_url, json=login_params, headers=headers,
                              cookies=cookies)
    # print(login_res.json())
    token = login_res.cookies
    token = {"cookies":
                 f"bccpgdhscfdate={token.get('bccpgdhscfdate')};"
                 f"CURRENT-LOGIN={token.get('CURRENT-LOGIN')};"
                 f"bccpgdhscf={token.get('bccpgdhscf')};"
                 f"CAPTCHAID={picCheckCodeKey}"
             }

    print("登录成功----获取token成功")
    YamlReader().write_yaml({"cookies": token})
    return token


# @pytest.fixture(scope="session", autouse=True)
# def get_sp_token_qy(init_pools, req_SP, conf_utill):
#     print("\n前置步骤----获取核心企业cookie")
#     global qy_token
#     redis_url = conf_utill.get_conf_redis()
#     rds = Redis(host=redis_url, port='6379', password='', decode_responses=True, db=116)
#     captcha_data = {'timestamp': int(round(time.time() * 1000))}
#     url = "tools-web/captcha/code/get"
#     res = req_SP.visit(method="GET", url=url, params=captcha_data)
#     picCheckCodeKey = res.cookies.get_dict()['CAPTCHAID']
#     # print(res.cookies.get_dict())
#     picCheckCode = rds.get(picCheckCodeKey)[1:5]
#     print("登陆验证码为 : " + picCheckCode)
#     username = conf_utill.get_qy_username()
#     password = conf_utill.get_qy_pwd()
#     login_params = {
#         "password": password,
#         "picCheckCode": picCheckCode,
#         "userName": username
#     }
#     headers = {'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '0'}
#     cookies = {'CAPTCHAID': picCheckCodeKey}
#     login_url = "sys-web/user/login"
#     login_res = req_SP.visit(method="POST", url=login_url, json=login_params, headers=headers,
#                              cookies=cookies)
#     # print(login_res.json())
#     lg_token = login_res.cookies
#     # print(lg_token)
#
#     # 验证码-phoneLogin 环节
#     pl_url = "/sys-web/user/phoneLogin"
#     pl_param = {
#         "userName": username,
#         "password": "1234"
#     }
#     rsp = req_SP.visit(method="POST", url=pl_url, json=pl_param, headers=headers,
#                        cookies=lg_token)
#     pl_token = rsp.cookies
#     qy_token = {"cookies":
#                     f"bccpgdhscfdate={pl_token.get('bccpgdhscfdate')};"
#                     f"CURRENT-LOGIN={pl_token.get('CURRENT-LOGIN')};"
#                     f"bccpgdhscf={pl_token.get('bccpgdhscf')};"
#                     f"DOUBLE_CHECK_TOKEN={lg_token.get('DOUBLE_CHECK_TOKEN')};"
#                     f"CAPTCHAID={picCheckCodeKey}"
#                 }
#
#     print("登录成功----获取token成功")
#     YamlReader().write_yaml({"qy_cookies": qy_token})
#     return qy_token

# if __name__ == '__main__':
#     recover_data()
