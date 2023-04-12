#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'
import pymysql

class DB():

    def __init__(self,db_config:dict):
        """
        连接数据库
        :param db_config:
        """
        self.connect = pymysql.connect(**db_config)

    def get_one(self,sql):
        """
        获取一条数据
        :return:
        """
        with self.connect.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()

    def get_many(self, sql, size:int):
        """
        获取多条数据
        :param sql:
        :param size:
        :return:
        """
        with self.connect.cursor()as cursor:
            cursor.execute(sql)
            return cursor.fetchmany(size)
    def get_all(self,sql):
        """
        获取所有数据
        :param sql:
        :return:
        """
        with self.connect.cursor()as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def exist(self,sql):
        """
        判断数据是否在数据库中存在
        :param sql:
        :return:
        """
        with self.connect.cursor()as cursor:
            cursor.execute(sql)
            if cursor.fetchone():
                return True
            else:
                return False

    def __del__(self):
        """
        析构函数，用于实现,对象被销毁时所执行的操作
        :return:
        """
        self.connect.close()






