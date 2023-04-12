#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'
import requests

def login(userName,passwordOrCode,corpId='2',loginType=1,source=1,rememberMe=False,systemFlag='LECAI',systemTerminalFlag=None):
    """
    登录运营平台
    :return:
    """
    url = "https://tes-platform.weihaizixun.com/tes/api/uac/account/loginIn"
    data = {"corpId": corpId,
            "loginType": loginType,
            "passwordOrCode": passwordOrCode,
            "source": source,
            "userName": userName,
            "rememberMe": rememberMe,
            "systemFlag": systemFlag,
            "systemTerminalFlag": systemTerminalFlag}
    headers = {'content-type': 'application/json'}
    try:
        reson = requests.post(url=url, json=data, headers=headers)
        if reson.status_code == 200:
            return reson.json()['data']
    except Exception as e:
        raise e

