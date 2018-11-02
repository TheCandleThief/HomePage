# coding: utf-8

"""
测试运行入口
2018.11.2
"""

__author__ = 'Cobb'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
