from . import TestCase
from test_module_function import models
from common import decorators
import time, re


class PersonalCenterTestCase(TestCase):
    """
    个人中心页测试用例

    注意，当前用例取消了自动关闭tab页的动作，所有的基于个人中心的页面都需要调用act_switch_self_handle方法
    """

    @classmethod
    def setUpClass(cls):
        TestCase.run_as = 'Chrome'
        TestCase.setUpClass()
        cls.personal_center = models.PersonalCenter(cls.driver, cls.config.URL.homepage_url)
        cls.login = models.Login(cls.driver)
        cls.login.act_login(cls.config.User.username, cls.config.User.password)
        cls.driver.find_element_by_id("header-login-nickname-str").click()

    def setUp(self):
        """将关闭浏览器标签的标志设置为False"""
        self.close_browser_current_tab_on_tear_down = False

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课随机点击开始学习失败")
    def test_job_course_learning_status(self):
        """测试就业课随机点击开始学习，进入播放课程列表"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        learning_study = self.personal_center.get_random_select_job_course_is_learning_status()
        course_name = learning_study.get_attribute("data-name")
        learning_study.click()

        course_title = self.driver.find_element_by_css_selector("div.course-title h1.normal")

        self.assertEqual(course_name, course_title.text,
                         "就业课点击开始学习失败，就业课列表显示的课程名称和实际课程名称不一致")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课点击课程已过期状态失败")
    def test_job_courses_expired(self):
        """测试就业课随机点击已过期的状态是否正确"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        job_courses_expired = self.personal_center.get_random_select_job_course_is_expired_status()
        job_courses_expired.click()

        tips_language = self.personal_center.get_expired_status_tips()[0]

        self.assertEqual("该课程已过期，续费请联系中心老师。", tips_language.text,
                         "点击已经过期的就业课状态，提示语有误")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课列表，点击课程名称进入就业课详情页失败")
    def test_job_course_details_page(self):
        """测试就业课列表，点击课程名称进入就业课详情页"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        job_course_name = self.personal_center.get_job_course_name(self.personal_center.get_random_select_job_course())
        a = job_course_name.text

        job_course_name.click()

        self.personal_center.act_switch_to_last_window()

        self.assertEqual("{0} - 岗位课 - 课工场".format(a), self.driver.title,
                         "就业课列表，点击课程名称进入就业课详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课-修改笔记失败")
    def test_job_course_modify_notes(self):
        """测试就业课-修改笔记功能"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        self.personal_center.get_job_course_notes(course).click()
        note = self.personal_center.get_select_job_course_note()
        index = self.personal_center.get_job_course_note_index(note)

        self.personal_center.act_job_course_note_edit(note)

        time.sleep(3)
        self.driver.refresh()
        note_content = self.personal_center.get_note_content(self.personal_center.get_select_job_course_note(index))

        self.assertEqual("修改笔记内容", note_content.text, "就业课修改笔记失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课-删除笔记失败")
    def test_job_course_del_notes(self):
        """测试就业课-删除笔记功能"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        self.personal_center.get_job_course_notes(course).click()
        note = self.personal_center.get_select_job_course_note()

        notes_number_first = len(self.personal_center.get_job_course_all_notes_or_QA_or_review())
        self.personal_center.act_job_course_note_del(note)
        notes_number_second = len(self.personal_center.get_job_course_all_notes_or_QA_or_review())

        self.assertEqual(notes_number_first, notes_number_second, "就业课-删除笔记失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课-笔记源自哪个课程进行跟踪失败")
    def test_job_couse_notes_from_which_course(self):
        """测试就业课-笔记源自哪个课程进行跟踪"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        self.personal_center.get_job_course_notes(course).click()
        note = self.personal_center.get_select_job_course_note()

        couse_notes_from_which_course = self.personal_center.get_job_couse_notes_from_which_course(note)

        name = couse_notes_from_which_course.text
        couse_notes_from_which_course.click()

        self.assertEqual("{0} - 课工场".format(name), self.driver.title, "就业课-笔记源自哪个课程进行跟踪失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课列表笔记数量和笔记详情页数量对比失败")
    def test_job_course_notes_number_compare(self):
        """就业课列表笔记数量和笔记详情页数量对比"""

        self.driver.back()

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        course_notes = self.personal_center.get_job_course_notes(course)
        course_notes_number = course_notes.text
        number_1 = re.sub("\D", "", course_notes_number)
        course_notes.click()

        number_2 = len(self.personal_center.get_job_course_all_notes_or_QA_or_review())

        self.assertEqual(int(number_1), number_2, "就业课列表笔记数量和笔记详情页数量对比失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课列表问答数量和问答详情页数量对比失败")
    def test_job_course_QA_number_compare(self):
        """就业课列表问答数量和问答详情页数量对比"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        course_question = self.personal_center.get_job_course_questions(course)
        course_question_number = course_question.text
        number_1 = re.sub("\D", "", course_question_number)

        course_question.click()

        number_2 = len(self.personal_center.get_job_course_all_notes_or_QA_or_review())

        self.assertEqual(int(number_1), number_2, "就业课列表问答数量和问答详情页数量对比失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课列表评论数量和评论详情页数量对比失败")
    def test_job_course_review_number_compare(self):
        """就业课列表评论数量和评论详情页数量对比失败"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        course_review = self.personal_center.get_job_course_comments(course)
        course_review_number = course_review.text
        number_1 = re.sub("\D", "", course_review_number)

        course_review.click()

        number_2 = len(self.personal_center.get_job_course_all_notes_or_QA_or_review())

        self.assertEqual(int(number_1), number_2, "就业课列表评论数量和评论详情页数量对比失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("测试笔记右上方点击进入就业课详情页失败")
    def test_job_course_notes_top_right_enter_the_job_course_details_page(self):
        """测试笔记右上方点击进入就业课详情页"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        self.personal_center.get_job_course_notes(course).click()

        right_course = self.personal_center.get_job_course_notes_top_right_enter_the_job_course_details_page()

        right_course_name = right_course.text
        right_course_name_a = re.split("：", right_course_name)

        right_course.click()

        self.assertEqual("{0} - 岗位课 - 课工场".format(right_course_name_a[1]),
                         self.driver.title, "测试笔记右上方点击进入就业课详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课-问答列表-进入问答详情页失败")
    def test_job_course_QA_enter_QA_details_pages(self):
        """测试就业课-问答列表-进入问答详情页"""

        self.driver.back()

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        self.personal_center.get_job_course_questions(course).click()
        time.sleep(3)

        QA = self.personal_center.get_select_job_course_note()
        QA_content = self.personal_center.get_QA_content(QA)
        QA_content_a = QA_content.text
        QA_content.click()

        self.personal_center.act_switch_to_last_window()

        self.assertIn(QA_content_a, self.driver.title, "就业课-问答列表-进入问答详情页失败")

    @decorators.TestCaseDecorators.screen_shot_in_except("就业课-问答列表-进入板块界面失败")
    def test_job_course_QA_plate_details_pages(self):
        """测试就业课-问答列表-进入板块界面"""

        self.personal_center.act_switch_to_self_handle()
        self.personal_center.refresh()
        self.personal_center.act_click_job()

        course = self.personal_center.get_random_select_job_course()
        self.personal_center.get_job_course_questions(course).click()
        time.sleep(3)

        QA = self.personal_center.get_select_job_course_note()
        QA_palte = self.personal_center.get_QA_palte(QA)

        QA_palte_name = QA_palte.text
        QA_palte.click()

        self.personal_center.act_switch_to_last_window()

        bbs_plate = models.BbsPlate(self.driver)
        plate_name = bbs_plate.get_plate_name().text

        self.assertEqual(QA_palte_name, "[{0}]".format(plate_name), "就业课-问答列表-进入板块界面失败")

















