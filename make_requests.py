#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import requests

def send_http_requests(method,url,**kwargs):
    """
    发送请求接口封装
    :param method:
    :param url:
    :param kwargs:
    :return:
    """
    return getattr(requests,method)(url=url,**kwargs)
