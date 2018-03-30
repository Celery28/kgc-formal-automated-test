from . import TestCase
from test_module_function import models
from common import decorators


class HomepageTestCase(TestCase):
    """
    课工场首页测试用例
    """

    homepage = None

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = "Chrome"
        TestCase.setUpClass()
        cls.homepage = models.Homepage(cls.driver, cls.config.URL.homepage_url)

    @decorators.TestCaseDecorators.screen_shot_in_except("进入课程库失败")
    def test_act_courses(self):
        """ 验证进入课程库界面"""
        self.homepage.act_switch_to_self_handle()
        self.homepage.act_courses()
        self.homepage.act_switch_to_last_window()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, self.config.URL.courses_url, "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("进入就业实训界面失败")
    def test_act_employment_base(self):
        """验证进入就业实训基地界面"""
        self.homepage.act_switch_to_self_handle()
        self.homepage.act_employment_base()
        self.homepage.act_switch_to_last_window()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, self.config.URL.a_kgc_cn_url, "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("进入岗位课界面失败")
    def test_act_job(self):
        """验证进入岗位课界面"""
        self.homepage.act_switch_to_self_handle()
        self.homepage.act_job()
        self.homepage.act_switch_to_last_window()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, self.config.URL.post_url, "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("进入金牌讲师界面失败")
    def test_act_teachers(self):
        """验证进入金牌讲师界面"""
        self.homepage.act_switch_to_self_handle()
        self.homepage.act_teachers()
        current_url = self.homepage.get_current_page_url()

        self.assertEqual(current_url, self.config.URL.teachers_url, "测试不通过")
