from . import TestSuite

from test_module_function import testcases

"""
岗位课测试套件

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""


class PostCourseTestSuite(TestSuite):

    def suites(self):
        # 【正式、test、dev环境已通过】

        # 验证进入岗位课详情页
        self.addTest(testcases.PostCoursesTestCase("test_post_course"))

        # 测试岗位课中随机进入课程详情页
        self.addTest(testcases.PostCourseTestCase("test_course_details_page"))
