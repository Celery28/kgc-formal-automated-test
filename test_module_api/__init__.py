import unittest
import os
import time

from test_module_api import testcases
from test_module_api import testsuites
from common.unittest_.runner import HTMLTestRunner

"""
API模块
"""


def main(opts):
    """
    API测试模块的主函数.

    :param opts:
    :return:
    """
    testcases.TestCase.set_environment(opts.environment)  # value of: development production pre-production
    all_test_suites = {_suite[:-9].lower(): _suite for _suite in testsuites.__dict__ if 'TestSuite' in _suite}

    suite = unittest.TestSuite()

    for suite_name in opts.suites or all_test_suites.keys():
        if suite_name.lower() not in all_test_suites.keys():
            raise NameError("无法找到对应的测试套件：{0}".format(suite_name))

        suite.addTests(testsuites.__dict__[all_test_suites[suite_name.lower()]]())

    if opts.report is False:
        runner = unittest.TextTestRunner()
    else:
        report_path = os.path.join(os.curdir, 'test_module_api', 'report')
        now = time.strftime('%Y-%m-%d %H-%M-%S')

        filename = os.path.join(report_path, now + 'report.html')
        fp = open(filename, 'wb')

        runner = HTMLTestRunner(stream=fp, title='课程库测试结果', description='测试报告.')

    runner.run(suite)
