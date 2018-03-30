import random

from selenium.common import exceptions

from . import Page


class PersonalCenter(Page):
    """
    个人中心
    """

    def is_exist_employment_courses(self):
        """
        判断是否存在就业课
        :return:
        """
        try:
            self.driver.find_element_by_css_selector("li.qd-job")
            return True
        except exceptions.NoSuchElementException:
            return False

    def act_click_job(self):
        """
        点击进入就业课tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-job a").click()

    def get_random_select_job_course(self):
        """
        随机选择一节就业课
        :return:
        """
        job_courses = self.driver.find_elements_by_css_selector("li.courseDetail")
        if len(job_courses) == 0:
            raise exceptions.NoSuchElementException("就业课列表没有找到任何就业课，请检查是否存在问题")
        return job_courses[random.randint(0, len(job_courses) - 1)]

    def get_random_select_job_course_is_learning_status(self):
        """
        随机选择就业课的学习状态=“开始学习”的就业课
        :return:
        """
        learning_status = self.driver.find_elements_by_link_text("开始学习")
        if len(learning_status) == 0:
            raise exceptions.NoSuchElementException("该账号下没有学习状态为正在学习的就业课")
        learning_study = learning_status[random.randint(0, len(learning_status) - 1)]

        return learning_study

    def get_random_select_job_course_is_expired_status(self):
        """
        随机选择就业课的学习状态=“课程已过期”的就业课
        :return:
        """
        expired_status = self.driver.find_elements_by_link_text("课程已过期")
        if len(expired_status) == 0:
            raise exceptions.NoSuchElementException("该账号下没有学习状态为课程已过期的就业课")
        job_courses_expired = expired_status[random.randint(0, len(expired_status) - 1)]

        return job_courses_expired

    def get_expired_status_tips(self):
        """
        已过期状态的就业课，温馨提示处理
        :return:
        """

        tips_language = self.driver.find_element_by_css_selector("div.recoverTip1 p")
        tips_yes = self.driver.find_element_by_css_selector("div.recoverTip1 a.yes")

        return tips_language, tips_yes

    def get_job_course_link(self, job_course):
        """
        获取就业课链接
        :param job_course:
        :return:
        """
        return job_course.find_element_by_css_selector("a.courseImg").get_attribute("href")

    def get_job_course_name(self, job_course):
        """
        获取就业课名称
        :param job_course:
        :return:
        """
        return job_course.find_element_by_css_selector("a.courseTitle")

    def get_job_course_status(self, job_course):
        """
        获取就业课学习状态
        :param job_course:
        :return: 开始学习 or 已过期
        """
        return job_course.find_element_by_css_selector("a.btn_study")

    def get_job_course_percentage(self, job_course):
        """
        获取就业课学习完成百分比
        :param job_course:
        :return:
        """
        return job_course.find_element_by_css_selector("div.courseInfo div.coursePro")

    def get_job_course_expired(self, job_course):
        """
        获取就业课过期时间
        :param job_course:
        :return:
        """
        return job_course.find_element_by_css_selector("div.courseInfo span")

    def get_job_course_notes(self, job_course):
        """
        获取就业课笔记
        :param job_course:
        :return:
        """
        return self._get_job_course_link(job_course, 'note', '没有找到笔记的链接')

    def get_job_course_questions(self, job_course):
        """
        获取就业课问答
        :param job_course:
        :return:
        """
        return self._get_job_course_link(job_course, 'ask', '没有找到问答的链接')

    def get_job_course_comments(self, job_course):
        """
        获取就业课评论
        :param job_course:
        :return:
        """
        return self._get_job_course_link(job_course, 'comment', '没有找到评论的链接')

    def get_job_course_tab_page(self):
        """
        进入就业课的tab页面
        就业课程
        学习计划
        我的自测
        :return:
        """
        job_course_tab_page = self.driver.find_element_by_css_selector("span.cen-note-t a")
        employment_courses = job_course_tab_page[0]
        study_play = job_course_tab_page[1]
        my_test = job_course_tab_page[2]

        return employment_courses, study_play, my_test

    def get_is_valid_learning_status(self):
        """
        获取有效的课程状态 = 开始学习
        :return:
        """

        learning_status = self.get_job_course_status(self.get_random_select_job_course()).text
        while learning_status is True:
            if learning_status == "开始学习":
                break
            else:
                learning_status = self.get_job_course_status(self.get_random_select_job_course()).text

    def get_job_course_all_notes_or_QA_or_review(self):
        """
        获取所有笔记或问答或评论
        :return:
        """
        return self.driver.find_elements_by_css_selector("ul.all-note li")

    def get_select_job_course_note(self, index=None):
        """
        随机选择课程笔记\问答\评论
        :param index:
        :return:
        """
        notes = self.get_job_course_all_notes_or_QA_or_review()
        if len(notes) == 0:
            raise exceptions.NoSuchElementException("该就业课下没有笔记")
        note = notes[index if index is not None else random.randint(0, len(notes) - 1)]

        return note

    def get_job_course_note_index(self, note):
        """
        获取笔记在笔记列表中的索引
        :param note:
        :return:
        """
        notes = self.get_job_course_all_notes_or_QA_or_review()

        for _note in notes:
            if note.find_element_by_css_selector('input[name=id]').get_attribute('value') \
                    == _note.find_element_by_css_selector('input[name=id]').get_attribute('value'):
                return notes.index(_note)

        raise exceptions.NoSuchElementException("没有在当前笔记列表找到该笔记")

    def get_note_content(self, note):
        """
        获取笔记内容
        :return:
        """

        note_content = note.find_element_by_css_selector("div.note-text")

        return note_content

    def act_job_course_note_edit(self, note):
        """
        修改就业课课程笔记
        :return:
        """
        note.find_element_by_css_selector("a.note-edit").click()

        input_box = self.driver.find_element_by_css_selector("textarea.p-note-area")
        input_box.clear()
        input_box.send_keys("修改笔记内容")

        self.driver.find_element_by_css_selector("button.note-save").click()

    def act_job_course_note_del(self, note):
        """
        删除就业课笔记
        :param note:
        :return:
        """

        note.find_element_by_css_selector("a.note-del").click()

        del_button = self.driver.find_element_by_css_selector("button.note-save")
        del_button.click()

    def get_job_couse_notes_from_which_course(self, note):
        """
        获取就业课-笔记源自哪个课程
        :param note:
        :return:
        """

        return note.find_element_by_css_selector("a.green")

    def get_job_course_notes_top_right_enter_the_job_course_details_page(self):
        """
        获取笔记右上方点击进入就业课详情页
        :return:
        """
        return self.driver.find_element_by_css_selector("div.center-note a.right")

    def get_QA_content(self, QA):
        """
        获取笔记内容
        :param QA:
        :return:
        """
        return QA.find_element_by_css_selector("a.black")

    def get_QA_palte(self, QA):
        """
        获取笔记所属板块
        :param QA:
        :return:
        """

        return QA.find_element_by_css_selector("a.green")



    """
    我的课程页面元素动作
    """

    def act_click_course(self):
        """
        点击进入课程tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-course").click()

    """
    个人动态页面元素动作
    """

    def act_click_news(self):
        """
        点击进入动态tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-news").click()

    """
    个人中心——题库页面元素动作
    """

    def act_click_question(self):
        """
        点击进入题库tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-square").click()

    """
    社区页面元素动作
    """

    def act_click_community(self):
        """
        点击进入社区tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-usercare").click()

    """
    任务页面元素动作
    """

    def act_click_task(self):
        """
        点击进入任务tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-task").click()

    """
    钱包页面元素动作
    """

    def act_click_wallet(self):
        """
        点击进入钱包tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-qnd").click()

    """
    设置页面元素动作
    """

    def act_click_set(self):
        """
        点击进入设置tab页
        :return:
        """
        self.driver.find_element_by_css_selector("li.qd-set").click()

    def _get_job_course_link(self, job_course, text, exception):
        """
        查找指定的链接
        :param job_course:
        :param text:
        :param exception:
        :return:
        """
        links = job_course.find_elements_by_css_selector("ul.courseNote li a")

        for link in links:
            if "{0}.shtml".format(text) in link.get_attribute("href"):
                return link
        raise exceptions.NoSuchElementException(exception)
