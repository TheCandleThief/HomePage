# coding: utf-8
"""
数据库工具类
时间：2018.04.27
"""
import os
import ConfigParser
from pymongo import MongoClient

__author__ = 'Cobb'

config = None

base_path = "\\".join(os.path.abspath(__file__).split('\\')[:-2])    # 获取到项目根目录

config_path = os.path.join(base_path, 'conf\glob.conf')


def get_conf():
    """
    配置
    """
    global config
    con_file = open(config_path)
    config = ConfigParser.ConfigParser()
    config.readfp(con_file)


class MongoUtil:
    def __init__(self):
        # print config.get('mongo', 'host'), config.get('mongo', 'db'), int(config.get('mongo', 'port'))
        self.client = MongoClient(config.get('mongo', 'host'), int(config.get('mongo', 'port')), connect=False)
        self.db = self.client[config.get('mongo', 'db')]

    # def verification_token(self, userId, token):
    #     self.collection = self.db['user']
    #     if self.collection.find({'userId': userId, 'token.token': token}).count() == 0:
    #         print 'MongoUtil False'
    #         return False
    #     else:
    #         print 'MongoUtil True'
    #         return True


get_conf()

