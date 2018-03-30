from . import TestCase
from test_module_function import models
from common import decorators


class CourseTestCase(TestCase):
    """
    课程测试用例
    """

    courses = None

    login = None

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()

        cls.courses = models.Courses(cls.driver, cls.config.URL.courses_url)
        cls.login = models.Login(cls.driver)
        cls.login.act_login(cls.config.User.username, cls.config.User.password)

    @decorators.TestCaseDecorators.screen_shot_in_except("验证免费课程购买失败")
    def test_free_course_buy(self):
        """
        免费课程购买测试用例.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        self.courses.act_close_sign_tip()
        self.courses.act_switch_price_filter_to_free()
        # self.courses.act_click_random_courses_page_url()

        course = self._get_effective_course([{'callback': 'is_allow_buy', 'result': True}])
        if course is None:
            self.close_browser_current_tab_on_tear_down = False
            raise Exception("本次测试没有找到可以购买的免费课程")

        course.act_click_buy_button()
        self.assertTrue(course.is_buy_success(), '验证免费课程购买失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("验证K币收费课程购买失败")
    def test_no_free_course_buy(self):
        """
        K币收费课程购买测试用例.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        self.courses.act_close_sign_tip()
        self.courses.act_switch_price_filter_to_no_free()
        # self.courses.act_click_random_courses_page_url()

        def _validate_course(course) -> bool:
            if course.is_allow_buy() is False:
                return False
            course.act_click_buy_button()
            if course.is_allow_buy_on_k_coins() is False:
                return False
            return True

        course = self._get_effective_course(_validate_course)
        if course is None:
            self.close_browser_current_tab_on_tear_down = False
            raise Exception("本次测试没有找到支持kb购买的课程")

        course.act_select_k_coins_pay_method()
        course.act_click_confirm_buy()
        self.assertTrue(course.is_buy_success(), '验证K币收费课程购买失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("课程关注验证失败")
    def test_course_favorite(self):
        """
        测试课程关注/取消关注.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        # self.courses.act_click_random_courses_page_url()
        self.courses.act_click_random_course()

        course = models.Course(self.driver)
        if course.is_favorite_for_course() is True:
            course.act_click_cancel_favorite()
            self.assertTrue(course.is_un_favorite_for_course(), '点击取消关注按钮失败')

            course.act_click_favorite()
            course.act_close_dialog()
            self.assertTrue(course.is_favorite_for_course(), '点击关注课程按钮失败')

        if course.is_un_favorite_for_course() is True:
            course.act_click_favorite()
            course.act_close_dialog()
            self.assertTrue(course.is_favorite_for_course(), '点击关注按钮失败')

            course.act_click_cancel_favorite()
            self.assertTrue(course.is_un_favorite_for_course(), '点击取消关注按钮失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("课程标签验证失败")
    def test_course_tag(self):
        """
        测试课程标签.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        # self.courses.act_click_random_courses_page_url()

        course = self._get_effective_course([{'callback': 'has_tag', 'result': True}])
        if course is None:
            self.close_browser_current_tab_on_tear_down = False
            raise Exception("本次测试没有找到拥有标签的课程")

        tag = course.get_random_tag()
        tag_name = tag.text

        tag.click()
        self.courses.act_switch_to_last_window()

        self.assertEqual("{0} - 标签 - 课工场".format(tag_name), self.driver.title, '验证标签失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("教师关注验证失败")
    def test_teacher_favorite(self):
        """
        测试教师关注/取消关注
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        # self.courses.act_click_random_courses_page_url()
        self.courses.act_click_random_course()

        course = models.Course(self.driver)
        if course.is_favorite_for_teacher() is True:
            course.act_click_favorite_for_teacher()
            self.assertTrue(course.is_un_favorite_for_teacher(), '点击取消关注教师按钮失败')

            course.act_click_favorite_for_teacher()
            self.assertTrue(course.is_favorite_for_teacher(), '点击关注教师按钮失败')

        if course.is_un_favorite_for_teacher() is True:
            course.act_click_favorite_for_teacher()
            self.assertTrue(course.is_favorite_for_teacher(), '点击关注教师按钮失败')

            course.act_click_favorite_for_teacher()
            self.assertTrue(course.is_un_favorite_for_teacher(), '点击取消关注教师按钮失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("验证教师点赞失败")
    def test_teacher_vote(self):
        """
        测试教师点赞.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        # self.courses.act_click_random_courses_page_url()

        course = self._get_effective_course([{'callback': 'is_vote_for_teacher', 'result': False}])
        if course is None:
            self.close_browser_current_tab_on_tear_down = False
            raise Exception("本次测试没有找到未点赞的教师")

        course.act_click_vote_for_teacher()
        self.assertTrue(course.is_vote_for_teacher(), '验证教师点赞失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("验证打开教师详情页失败")
    def test_open_teacher(self):
        """
        测试打开教师详情页.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        # self.courses.act_click_random_courses_page_url()
        self.courses.act_click_random_course()

        course = models.Course(self.driver)
        teacher_name = course.get_teacher_name()

        course.act_click_teacher_name()
        self.assertEqual("{0} - 讲师 - 课工场".format(teacher_name), self.driver.title, '验证点击教师失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("测试添加课程评价失败")
    def test_course_commit(self):
        """
        测试课程评价.
        
        :return: 
        """
        self.courses.act_switch_to_self_handle()
        # self.courses.act_click_random_courses_page_url()
        self.courses.act_click_random_course()

        course = models.Course(self.driver)
        course.act_switch_to_comment_tab()

        # TODO:未完成

    def _get_effective_course(self, validate_callbacks: list):
        """
        获取一个有效课程.
        
        :param validate_callbacks: 验证方法的回调方法列表或者回调函数
            [{'callback': 方法名称}, ...] or def callback(course) -> bool: pass
        :return: 
        """
        for i in range(0, 3):
            self.courses.act_switch_to_self_handle()
            self.courses.act_click_random_course()

            course = models.Course(self.driver)
            if isinstance(validate_callbacks, list):
                allow = True
                for callback in validate_callbacks:
                    if not models.Course.__dict__[callback['callback']](course) is callback['result']:
                        course.close()
                        allow = False
                        break
                if allow is False:
                    continue
            elif callable(validate_callbacks):
                if validate_callbacks(course) is False:
                    course.close()
                    continue
            return course
        return None
