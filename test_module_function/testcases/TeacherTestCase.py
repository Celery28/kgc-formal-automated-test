from . import TestCase
from test_module_function import models
from common import decorators


class TeacherTestCase(TestCase):
    """
    教师详情页测试用例
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.teachers = models.Teachers(cls.driver, cls.config.URL.teachers_url)
        cls.login = models.Login(cls.driver)
        cls.login.act_login(cls.config.User.username, cls.config.User.password)

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_教师关注验证失败")
    def test_teacher_details_favorite(self):
        """
        测试教师关注/取消关注
        :return: 
        """
        self.teachers = models.Teachers(self.driver, self.config.URL.teachers_url)
        self.teachers.act_click_random_teacher()
        teacher = models.Teacher(self.driver)
        if teacher.is_favorite_for_teacher() is True:
            teacher.act_click_cancel_favorite()
            self.assertTrue(teacher.is_un_favorite_for_teacher(), '点击取消关注教师按钮失败')

            teacher.act_click_favorite()
            self.assertTrue(teacher.is_favorite_for_teacher(), '点击关注教师按钮失败')

        if teacher.is_un_favorite_for_teacher() is True:
            teacher.act_click_favorite()
            self.assertTrue(teacher.is_favorite_for_teacher(), '点击关注教师按钮失败')

            teacher.act_click_cancel_favorite()
            self.assertTrue(teacher.is_un_favorite_for_teacher(), '点击取消关注教师按钮失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_教师点赞验证失败")
    def test_teacher_zan(self):
        """
        测试教师点赞
        :return:
        """
        # self.teachers = models.Teachers(self.driver, self.config.URL.teachers_url)

        teacher = self._get_effective_teacher([{'callback': 'is_vote_for_teacher', 'result': False}])
        if teacher is None:
            self.close_browser_current_tab_on_tear_down = False
            raise Exception("本次测试没有找到未点赞的教师")
        teacher.act_click_vote_for_teacher()

        self.assertTrue(teacher.is_vote_for_teacher(), '验证教师点赞失败')

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_随机进入同方向讲师失败")
    def test_same_direction_teacher(self):
        """
        验证随机进入同方向讲师
        :return:
        """
        self.teachers = models.Teachers(self.driver, self.config.URL.teachers_url)
        teacher = self._get_effective_teacher([{'callback': 'has_same_teacher_direction', 'result': True}])
        if teacher is None:
            self.close_browser_current_tab_on_tear_down = False
            raise Exception("本次测试没有找到有同方向的讲师")

        same_teacher = teacher.get_random_same_teacher_direction()
        same_teacher_name = teacher.get_teacher_name(same_teacher)
        same_teacher.click()

        self.assertEqual(self.driver.title(), "{0} - 讲师 - 课工场".format(same_teacher_name), "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("教师详情页_随机进入金牌讲师失败")
    def test_gold_medal_teacher(self):
        """
        验证随机进入金牌讲师失败
        :return:
        """

        pass

    # def _get_effective_teacher_a(self):
    #     """
    #     获取一个未点赞的有效教师.
    #
    #     :return:
    #     """
    #     for i in range(0, 3):
    #         self.teachers.act_click_select_teacher_again()
    #
    #         teacher = models.Teacher(self.driver)
    #         if teacher.is_vote_for_teacher() is True:
    #             teacher.close()
    #             continue
    #         return teacher
    #     return None

    def _get_effective_teacher(self, validate_callbacks: list):
        """
        获取一个有效教师.

        :param validate_callbacks: 验证方法的回调方法列表或者回调函数
            [{'callback': 方法名称}, ...] or def callback(course) -> bool: pass
        :return:
        """

        for i in range(0, 3):
            self.teachers.act_click_random_category()
            teacher = self.teachers.get_random_teacher()
            if teacher is None:
                continue
            self.teachers.get_teacher_info(teacher)[1].click()
            teacher = models.Teacher(self.driver)
            if isinstance(validate_callbacks, list):
                allow = True
                for callback in validate_callbacks:
                    if not models.Teacher.__dict__[callback['callback']](teacher) is callback['result']:
                        allow = False
                        break
                if allow is False:
                    self.driver.back()
                    continue
            return teacher

        return None






