from test_module_function import models
from . import TestCase
from common import decorators
import re


class PostCourseTestCase(TestCase):
    """
    岗位详情页测试用例.
    
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.post_courses = models.PostCourses(cls.driver, cls.config.URL.post_url)

    @decorators.TestCaseDecorators.screen_shot_in_except("点击进入下一课失败")
    def test_next_course(self):
        """
        测试进入下一课
    
        :return:
        """
        pass
        # course = self.post_courses.act_click_random_post_course()
        #
        # if course.has_next_course() is False:
        #     pass
        #
        # course.act_click_next_course()
        # self.assertIn('', '', '')

    @decorators.TestCaseDecorators.screen_shot_in_except("岗位课中随机进入课程详情页失败")
    def test_course_details_page(self):
        """
        测试岗位课中随机进入课程详情页
        :return:
        """

        # 随机选择岗位课
        self.post_courses.act_click_random_post_course()

        post_course = models.PostCourse(self.driver)

        # 随机选择章节并点击
        course_chapter = post_course.get_random_post_courses_course_chapters()

        course = post_course.get_random_post_courses_course_details_page(course_chapter)
        course_message = post_course.get_course_message(course)

        course_url = course_message[1]
        course_url = re.sub("\D", "", course_url)

        # 进入课程详情页
        post_course.act_click_course(course)

        self.post_courses.act_switch_to_last_window()

        course_url_new = self.post_courses.get_current_page_url()
        course_url_new = re.sub("\D", "", course_url_new)

        self.assertEqual(course_url, course_url_new, "岗位课中随机进入课程详情页失败")

