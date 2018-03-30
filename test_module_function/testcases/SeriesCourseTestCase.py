from . import TestCase
from test_module_function import models
from common import decorators


class SeriesCourseTestCase(TestCase):
    """
    系列集合页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.series_course = models.SeriesCourse(cls.driver, cls.config.URL.series_course_url)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""

        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("系列课随机进入某节课程失败")
    def test_series_course(self):
        """测试系列课随机进入某节课程"""

        series_course = self.series_course.get_random_series_course()[1]
        series_course_message = self.series_course.get_series_course_message(series_course)

        course_name = series_course_message[0].text
        series_course_message[2].click()

        self.series_course.act_switch_to_last_window()

        self.assertEqual("{0} - 课工场".format(course_name), self.driver.title, "系列课随机进入某节课程失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("验证系列课课程数量失败")
    def test_series_course_number(self):
        """测试系列课程数量"""

        series_course_number = self.series_course.get_series_course_number().text
        series_courses_len = self.series_course.get_random_series_course()[0]

        self.assertEqual(int(series_course_number), series_courses_len, "验证系列课课程数量失败")






