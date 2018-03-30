from . import TestCase
from test_module_function import models
from common import decorators


class PostCoursesTestCase(TestCase):
    """
    岗位课列表用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.post_courses = models.PostCourses(cls.driver, cls.config.URL.post_url)

    @decorators.TestCaseDecorators.screen_shot_in_except("随机进入岗位课详情页失败")
    def test_post_course(self):
        """
        随机进入岗位课详情页

        :return:
        """
        random_course = self.post_courses.get_random_post_course()
        url = random_course.get_attribute('href')

        random_course.click()
        self.post_courses.act_switch_to_last_window()
        self.assertIn(url, self.driver.current_url, "测试不通过")


