#!/usr/bin/env python3
# _._ coding:utf-8 _._

"""
课工场自动化测试主入口文件

测试以模块为单位对具体业务进行测试，通过建立模块并注册在映射表中可以添加新的模块
每个模块应该时一个包，在该包的__init__.py文件中实现该模块的主入口函数，并将该函数添加到映射表中
已安装的模块如下：
    function   自动化功能测试模块
    api        自动化APP接口测试模块

使用方法:
    自动化功能测试
        python3 main.py function -e production -r   正式环境，生成测试报告，所有套件
        python3 main.py function -ss Course     dev环境，不生成测试报告，CourseTestSuite套件

:python version: ~3.6.0
:requests version: ~2.18.0
:author: ronghui.huo <ronghui.huo@kgc.cn>
"""

import os
import argparse

import test_module_function
import test_module_api

parser = argparse.ArgumentParser()
parser.add_argument('module', help='执行的测试模块。可选值：function api')
parser.add_argument('-e', '--environment', default='development',
                    help='运行的测试环境，默认为：development。可选值：development pre-production production')
parser.add_argument('-r', '--report', action="store_true", help='生成HTML测试报告')
parser.add_argument('-ss', '--suites', default=[], nargs='*', help='设置运行的测试套件，若不设置则执行所有套件')
opts = parser.parse_args()

if __name__ == '__main__':
    modules = {'function': test_module_function.main, 'api': test_module_api.main}

    if opts.module not in modules:
        raise ValueError('无效的模块参数:{0}'.format(opts.module))

    modules[opts.module](opts)
