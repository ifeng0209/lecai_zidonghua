#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import unittest
from common.HTMLTestRunner import HTMLTestRunner
import settings
from common.report_handler import report

if __name__ == '__main__':
    #收集测试用例，生成测试套件，执行用例，生成测试报告

    ts = unittest.TestLoader().discover('test_cases')
    report(ts, **settings.REPORT_CONFIG)

