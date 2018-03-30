from . import TestCase
from test_module_function import models
from common import decorators


class TeachersTestCase(TestCase):
    """
    教师列表页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.teachers = models.Teachers(cls.driver, cls.config.URL.teachers_url)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("随机选择教师方向失败")
    def test_teachers_category(self):
        """随机筛选教师方向"""
        teacher_category = self.teachers.get_random_teachers_category()
        click_category_name = teacher_category.text
        teacher_category.click()

        category_name = self.teachers.get_current_teachers_category().text
        self.assertEqual(click_category_name, category_name, "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("随机进入教师详情页失败")
    def test_teachers_page(self):
        """随机进入教师详情页"""

        teacher = self.teachers.get_random_teacher()

        while teacher is None:
            self.teachers.act_click_random_category()
            teacher = self.teachers.get_random_teacher()

        teacher_name, teacher_classroom = self.teachers.get_teacher_info(teacher)
        teacher_classroom.click()

        self.assertEqual(self.driver.title, "{0} - 讲师 - 课工场".format(teacher_name), "测试不通过")



