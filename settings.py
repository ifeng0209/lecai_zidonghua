#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import os


#根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#项目域名
PROJECT_HOST = 'https://tes-platform.weihaizixun.com/tes/api'

#接口名称
INTERFACES = {
    'CREATE':'/elephantstep/xlc-ops-b/elephantstep/web/app/create'
}



#日志配置文件

LOG_CONFIG = {
    'name':'elephant',
    'filename': os.path.join(BASE_DIR, 'logs/象步的测试日志.log'),
    'encoding':'utf-8',
    'mode':'a',
    'debug':True
}


# 测试报告
REPORT_CONFIG = {
    'description': '象步测试报告',  #测试报告描述
    'filename': '象步测试报告.html', #测试报告标题
    'report_dir': os.path.join(BASE_DIR, 'reports'), #测试报告路径
    'title': '象步项目', #测试报告标题
    'theme': 'theme_default',#报告主题
    '_type': 'br'
}

#数据库配置--象步
DB_ELEPHANT_CONFIG ={
    'host': 'pc-2zej1sknw83e34ik2.rwlb.rds.aliyuncs.com', #ip地址
    'user': 'test_codeuse',#用户名
    'password': '2hCW2y3q72r7!zR',#密码
    'db': 'test_elephant_step',#库名
    'charset': 'utf8',#字符集，默认为utf8，注意不是utf-8
    'port': 3306,#端口号，默认为3306
    'autocommit': True  # 自动提交事务 防止可重复读的问题
}

















