#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import os
from datetime import datetime
from BeautifulReport import BeautifulReport
from common.HTMLTestRunner import HTMLTestRunner

def report(ts,filename,report_dir,theme='theme_default',title=None,description=None,tester=None,_type='br'):
    """
    生成测试报告
    :param ts: 测试套件
    :param filename: 报告文件名
    :param file_dir: 报告路径br
    :param theme: 报告主题 br
    :param title: 报告标题 html
    :param description: 报告描述
    :param tester: 报告执行人员html
    :param _type: 报告类型
    :return:
    """

    #报告文件名前缀
    file_suffix= datetime.now().strftime('%Y%m%d%H%M%S')

    #报告文件名整体拼接
    filename='{}_{}'.format(file_suffix,filename)

    if _type=='br':
        runner = BeautifulReport(ts)
        runner.report(filename=filename,report_dir=report_dir,theme=theme,description=description)
    else:
        with open(os.path.join(report_dir,filename),'wb')as f:
            runner = HTMLTestRunner(f,description=description,title=title,tester=tester)
            runner.run(ts)



























