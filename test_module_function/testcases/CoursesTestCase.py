from . import TestCase
from test_module_function import models
from common import decorators


class CoursesTestCase(TestCase):
    """
    课程库测试用例
    """

    courses = None

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.courses = models.Courses(cls.driver, cls.config.URL.courses_url)

    def setUp(self):
        """
        将关闭浏览器标签的标志设置为False.

        :return:
        """
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("课程库课程数量验证失败")
    def test_courses_number(self):
        """
        测试课程页的课程数量.

        :return:
        """
        self.assertEqual(25, self.courses.get_current_page_course_count(), '课程库列表的课程数量错误')

    @decorators.TestCaseDecorators.screen_shot_in_except("课程方向验证失败")
    def test_first_category(self):
        """
        随机进入课程方向测试
        :return:
        """

        self.courses.act_click_random_first_category()
        category = self.courses.get_current_first_category()
        self.assertEqual("{0} - 课工场".format(category.text), self.courses.get_current_title(), '测试不通过')

    @decorators.TestCaseDecorators.screen_shot_in_except("课程分类验证失败")
    def test_sub_category(self):
        """
        随机进入课程分类测试
        :return:
        """

        self.courses.act_click_random_sub_category()
        category = self.courses.get_current_sub_category()

        # TODO: 这个验证规则不稳定，需要优化
        self.assertIn(category.text, self.courses.get_current_title(), '测试不通过')

    @decorators.TestCaseDecorators.screen_shot_in_except("测试筛选课程最新最热状态失败")
    def test_courses_sort(self):
        """
        验证最新最热筛选功能
        :return: 
        """

        self.courses.act_switch_courses_sort_to_hot()
        sort = self.courses.get_current_courses_sort()
        self.assertEqual("最热", sort.text, "测试不通过")

        self.courses.act_switch_courses_sort_to_new()
        sort = self.courses.get_current_courses_sort()
        self.assertEqual("最新", sort.text, "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("筛选收费免费课程失败")
    def test_courses_price_filter(self):
        """
        验证收费与免费过滤器.
        
        :return: 
        """

        self.courses.act_switch_price_filter_to_free()
        level = self.courses.get_current_courses_price_filter()
        self.assertEqual("免费", level.text, "测试不通过")

        self.courses.act_switch_price_filter_to_no_free()
        level = self.courses.get_current_courses_price_filter()
        self.assertEqual("付费", level.text, "测试不通过")

    @decorators.TestCaseDecorators.screen_shot_in_except("筛选课程难度等级失败")
    def test_course_difficulty_level(self):
        """
        随机筛选课程难度等级
        
        :return: 
        """

        self.courses.act_switch_courses_difficulty_level_to_zero_based()
        level = self.courses.get_current_courses_difficulty_level_filter()
        self.assertEqual("零基础", level.text, "测试不通过")

        self.courses.act_switch_courses_difficulty_level_to_based()
        level = self.courses.get_current_courses_difficulty_level_filter()
        self.assertEqual("基础", level.text, "测试不通过")

        self.courses.act_switch_courses_difficulty_level_to_middle_level()
        level = self.courses.get_current_courses_difficulty_level_filter()
        self.assertEqual("中级", level.text, "测试不通过")

        self.courses.act_switch_courses_difficulty_level_to_high_level()
        level = self.courses.get_current_courses_difficulty_level_filter()
        self.assertEqual("高级", level.text, "测试不通过")

        self.courses.act_switch_courses_difficulty_level_to_all_level()
        level = self.courses.get_current_courses_difficulty_level_filter()
        self.assertEqual("全部", level.text, "测试不通过")
