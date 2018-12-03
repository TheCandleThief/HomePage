# coding=utf-8
"""
工具类：加密、
时间：2018.04.27
"""
import hashlib

__author__ = 'Cobb'


def verification_args(args_list, request):
    """
    验证参数合法
    :param args_list: 参数列表
    :param request:请求
    :return:如果合法返回True,反之返回False
    """
    for arg in args_list:
        if not request or arg not in request.form or not request.form[arg]:
            return False
        else:
            continue
    return True


def to_hash(text):
    """
    md5加密
    :param text: 待加密的文本
    :return: 加密后的文本
    """
    m = hashlib.md5()        # 创建一个MD5加密对象
    m.update(text)           # 更新要加密的数据
    return m.hexdigest()     # 加密后的结果，用十六进制字符串表示。