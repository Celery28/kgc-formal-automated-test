from . import TestSuite

from test_module_function import testcases

"""
系列课测试套件

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""


class SeriesTestSuite(TestSuite):

    def suites(self):
        # 测试系列课程数量
        self.addTest(testcases.SeriesCourseTestCase("test_series_course_number"))

        # 测试系列课随机进入某节课程
        self.addTest(testcases.SeriesCourseTestCase("test_series_course"))
