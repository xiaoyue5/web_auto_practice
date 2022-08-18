"""
    @ describe:
    @ author:xiaoyue
    @ version:1.0.0
    @ copyright:yue
    @ datetime:2022/8/15 14:07
    
"""
import pymysql
import os
from utils.my_path import CONF_PATH
from utils.my_conf import MyConf
from utils.my_logging import logger


class MyMysql:
    def __init__(self):
        my_conf = MyConf(os.path.join(CONF_PATH, "mysql.ini"))
        mysql = "mysql1"
        self.connect = None
        self.cursor = None
        try:
            self.connect = pymysql.connect(user=my_conf.get(mysql, "user"),
                                           host=my_conf.get(mysql, "host"),
                                           database=my_conf.get(mysql, "database"),
                                           port=my_conf.getint(mysql, "port"),
                                           password=my_conf.get(mysql, "password"),
                                           cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connect.cursor()
        except Exception as e:
            logger.info(e)
        pass

    def execute(self, sql: str):
        """
        执行sql语句
        :param sql: 要执行的sql语句
        :return: 查询语句返回查询到的所有结果，其他语句返回受到影响的行数
        """
        is_select = False
        if sql.lower().startswith("select"):
            is_select = True
        try:
            self.cursor.execute(sql)
            if is_select:
                return self.cursor.fetchall()
            else:
                self.connect.commit()
                return self.cursor.rowcount
        except Exception as e:
            self.connect.rollback()
            logger.info(e)
        finally:
            self.close()

    def close(self):
        self.cursor.close()
        self.connect.close()
