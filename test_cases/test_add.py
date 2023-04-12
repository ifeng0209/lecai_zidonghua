#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'
from common.make_requests import send_http_requests
from common.fixture import login
from common.myddt import data, ddt

import unittest
import json

cases = {'id': 1,
         'method': 'post',
         'title': '新增应用菜单',
         'request': {
             'data': {"appName": "test-001", "showName": "test-001", "logoUrl": "", "linkUrl": "", "siteUrl": "","appStatus": 0, "lang": "zh-cn", "tenantId": "2", "uid": 481154},
             'headers': {"content-type": "application/json", "sso_sys_token": "#token#"}},
         'expect_data':{"code":0,"msg":"成功"}}



@ddt
class TestAdd(unittest.TestCase):


    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:

        #----fixture 封装登录接口

        reson = login(userName='18848959685', passwordOrCode='joyhr@2022')
        cls.token = reson['token']


    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @data(*cases)
    def test_add(self,case):
        """
        新增菜单
        :return:
        """
        #----改为从excel中读取测试数据----
        #----菜单名称写死了，要每次不一样----
        if '#token#' in case['request']:
            case['request'] = case['request'].replace('#token#', self.token)

        case['url'] = 'https://tes-platform.weihaizixun.com/tes/api/elephantstep/xlc-ops-b/elephantstep/web/app/create'
        case['request'] = json.loads(case['request'])
        case['expect_data'] = json.loads(case['expect_data'])

        res = send_http_requests(method=case['method'],url=case['url'],**case['request'])
        print(res.json())




