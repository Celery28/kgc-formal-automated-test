from . import TestCase
from test_module_function import models
from common import decorators


class SearchTestCase(TestCase):
    """
    搜索测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.search = models.Search(cls.driver, cls.config.URL.search_url)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""

        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索失败")
    def test_search_course(self):
        """搜索课程"""

        self.search.get_search_content()

        self.search.driver.find_element_by_xpath(self.search.course).click()
        self.assertTrue(self.search.is_null_search(), "当前搜索词未搜索出相关课程，测试失败，请重试")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索帖子失败")
    def test_search_post(self):
        """搜素帖子"""

        self.search.get_search_content()

        self.search.driver.find_element_by_xpath(self.search.post).click()
        self.assertTrue(self.search.is_null_search(), "当前搜索词未搜索出相关帖子，测试失败，请重试")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索老师失败")
    def test_search_teacher(self):
        """搜索老师"""

        self.search.get_search_content()

        self.search.driver.find_element_by_xpath(self.search.teacher).click()
        self.assertTrue(self.search.is_null_search(), "当前搜索词未搜索出相关老师，测试失败，请重试")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索学友失败")
    def test_search_student(self):
        """搜素学友"""

        self.search.get_search_content()

        self.search.driver.find_element_by_xpath(self.search.user).click()
        self.assertTrue(self.search.is_null_search(), "当前搜索词未搜索出相关学友，测试失败，请重试")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索课程进入课程详情页失败")
    def test_search_course_enter_course_details_page(self):
        """测试搜索课程进入课程详情页"""

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.course).click()

        course_name = self.search.get_course_message(self.search.get_random_course_for_search_courses())
        course_name_a = course_name.text
        course_name.click()

        self.assertEqual("{0} - 课工场".format(course_name_a), self.driver.title, "搜索课程进入课程详情页测试失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索课程进入标签详情页失败")
    def test_search_course_enter_label_details_page(self):
        """测试搜索课程进入标签详情页"""

        self.driver.back()

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.course).click()

        course_label = self.search.get_random_course_label_for_courses()
        course_label_name = course_label.text
        course_label.click()

        self.assertEqual("{0} - 标签 - 课工场".format(course_label_name), self.driver.title, "搜索课程进入标签详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索课程翻页功能失败")
    def test_search_course_flip_pages(self):
        """测试搜索课程翻页功能"""

        self.driver.back()

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.course).click()

        self.search.get_random_flip_pages().click()

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索帖子随机进入帖子详情页失败")
    def test_search_post_enter_post_details_page(self):
        """测试搜索帖子随机进入帖子详情页"""

        self.driver.back()

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.post).click()

        post_content = self.search.get_post_message(self.search.get_random_post_for_posts())[0]
        post_content_a = post_content.text
        post_content.click()

        self.assertIn(post_content_a, self.driver.title,  "搜索帖子随机进入帖子详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索帖子随机进入板块详情页失败")
    def test_search_post_enter_plate_details_page(self):
        """测试搜索帖子随机进入板块详情页失败"""

        self.driver.back()

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.post).click()

        post_plate = self.search.get_post_message(self.search.get_random_post_for_posts())[1]
        post_plate_name = post_plate.text
        post_plate.click()

        self.assertEqual("{0} - 课工场".format(post_plate_name), self.driver.title, "搜索帖子随机进入板块详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索帖子进入个人主页失败")
    def test_search_post_enter_homepage(self):
        """测试搜索帖子随机进入个人主页"""

        self.driver.back()

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.post).click()

        homepage, homepage_url = self.search.get_post_message(self.search.get_random_post_for_posts())[2:]
        homepage.click()

        self.search.act_switch_to_last_window()

        self.assertEqual(homepage_url, self.driver.current_url, "搜索帖子进入个人主页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索教师随机进入教师主页失败")
    def test_search_teacher_enter_teacher_homepage(self):
        """测试搜索教师进入教师主页"""

        self.driver.switch_to.window(self.driver.window_handles[0])

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.teacher).click()

        teacher_message = self.search.get_teacher_message(self.search.get_random_teacher_for_teachers())

        teacher_name = teacher_message[2].text
        teacher_message[0].click()

        self.assertEqual("{0} - 讲师 - 课工场".format(teacher_name), self.driver.title, "搜索教师随机进入教师主页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("搜索学友随机进入个人主页失败")
    def test_search_user_enter_homepage(self):
        """测试搜索学友随机进入个人主页"""

        self.driver.back()

        self.search.get_search_content()
        self.search.driver.find_element_by_xpath(self.search.user).click()

        student_message = self.search.get_student_message(self.search.get_random_student_for_students())

        user_name = student_message[2].text
        student_message[0].click()

        self.search.act_switch_to_last_window()

        self.assertEqual("{0}参加的课程 - 课工场".format(user_name), self.driver.title, "搜索学友随机进入个人主页失败")




















