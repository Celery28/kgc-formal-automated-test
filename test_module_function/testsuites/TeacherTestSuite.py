from . import TestSuite

from test_module_function import testcases

"""
教师测试套件

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""


class TeacherTestSuite(TestSuite):

    def suites(self):
        # 教师列表页测试用例【正式、test、dev环境已通过】

        # 验证随机筛选教师方向
        self.addTest(testcases.TeachersTestCase("test_teachers_category"))

        # 随机进入教师详情页
        self.addTest(testcases.TeachersTestCase("test_teachers_page"))

        # 教师详情页测试用例

        # 验证教师详情页关注功能
        self.addTest(testcases.TeacherTestCase("test_teacher_details_favorite"))

        # 验证教师点赞功能
        self.addTest(testcases.TeacherTestCase("test_teacher_zan"))

        # 验证随机进入同方向讲师
        self.addTest(testcases.TeacherTestCase("test_same_direction_teacher"))

        # 验证随机进入金牌讲师页面
        self.addTest(testcases.TeacherTestCase("test_gold_medal_teacher"))
