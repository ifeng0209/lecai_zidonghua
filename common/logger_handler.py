#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import logging

def get_logger(name,filename,mode='a',encoding='utf-8',fmt=None,debug=False):
    """
    :param name:日志器
    :param filename:日志要写入的文件
    :param mode:追加模式
    :param encoding:编码
    :param fmt:格式化
    :param debug:调试模式
    :return:
    """
    #日志记录器
    logger =logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    #控制台输出的日志要详细

    if debug:
        file_level=logging.DEBUG
        console_level =logging.DEBUG
    else:
        file_level =logging.DEBUG
        console_level=logging.INFO

    if fmt is None:
        fmt = '%(levelname)s %(asctime)s [%(filename)s-->line:%(lineno)d]:%(message)s'

    #文件处理器
    file_handler =logging.FileHandler(filename=filename,mode=mode,encoding=encoding)
    file_handler.setLevel(file_level)

    #控制台日志处理器
    console_handler =logging.StreamHandler()
    console_handler.setLevel(console_level)

    #格式化器
    formatter =logging.Formatter(fmt=fmt)

    # #文件处理器和日志处理器设置格式化
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将文件处理器和日志处理器添加到日志记录器中

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger




if __name__ == '__main__':
    logger = get_logger(name='py38', filename='../logs/py38.log', debug=True)
    logger.info('我是普通信息')





















