from . import TestSuite

from test_module_function import testcases

"""
个人中心测试套件

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""


class PersonalCenterTestSuite(TestSuite):

    def suites(self):
        # 测试就业课列表，点击课程名称进入就业课详情页
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_details_page"))

        # 测试就业课随机点击开始学习，进入播放课程列表
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_learning_status"))

        # 测试就业课随机点击已过期状态，弹出正确的提示语
        self.addTest(testcases.PersonalCenterTestCase("test_job_courses_expired"))

        # 测试就业课-修改、删除笔记功能
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_modify_notes"))
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_del_notes"))

        # 测试就业课-笔记源自哪个课程进行跟踪
        self.addTest(testcases.PersonalCenterTestCase("test_job_couse_notes_from_which_course"))

        # 测试就业课列表笔记、问答、评论数量和笔记详情页数量对比
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_notes_number_compare"))
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_QA_number_compare"))
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_review_number_compare"))

        # 测试笔记右上方点击进入就业课详情页
        self.addTest(
            testcases.PersonalCenterTestCase("test_job_course_notes_top_right_enter_the_job_course_details_page"))

        # 测试就业课-问答列表-进入问答详情页
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_QA_enter_QA_details_pages"))

        # 测试就业课-问答列表-进入板块详情页
        self.addTest(testcases.PersonalCenterTestCase("test_job_course_QA_plate_details_pages"))
