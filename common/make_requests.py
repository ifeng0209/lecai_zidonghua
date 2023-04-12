#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import requests

def send_http_requests(method,url,**kwargs)->requests.Response:
    """
    发送请求接口封装
    :param method:
    :param url:
    :param kwargs:
    :return:
    """
    return getattr(requests,method)(url=url,**kwargs)


if __name__ == '__main__':
    data = {"corpId": "2", "loginType": 1, "passwordOrCode": "joyhr@2022", "source": 1, "userName": "18848959685",
            "rememberMe": True, "systemFlag": "LECAI", "systemTerminalFlag": ""}
    url = "https://tes-platform.weihaizixun.com/tes/api/uac/account/loginIn"
    headers = {
        "Connection": "keep-alive",
        "Content-Length": "157",
        "Origin": "https://tes-platform.weihaizixun.com",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://tes-platform.weihaizixun.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    res = send_http_requests('post', url=url, json=data, headers=headers)
    print(res.json(),type(res))
    print(res.cookies)

