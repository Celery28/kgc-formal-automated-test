import random

from . import Page

from selenium.common import exceptions


class Teachers(Page):
    """
    教师列表页模型
    """

    url = 'http://www.kgc.dev.cn/teachers'

    def is_exist_teacher_in_direction(self):
        """
        判断方向下是否存在讲师
        :return:
        """
        try:
            self.driver.find_elements_by_css_selector("ul.teacher-list li")
            return True
        except exceptions.NoSuchElementException:
            return False

    def get_random_teachers_category(self):
        """
        随机获取教师方向

        :return:
        """
        teachers_category = self.driver.find_elements_by_css_selector("div.yui3-u-7-8 li")
        if len(teachers_category) == 0:
            raise exceptions.NoSuchElementException("没有找到课程方向")

        teacher_category = teachers_category[random.randint(1, len(teachers_category) - 1)]

        return teacher_category

    def get_current_teachers_category(self):
        """
        获取当前选中的教师方向名称

        :return:
        """
        category_name = self.driver.find_elements_by_css_selector("div.yui3-u-7-8 li a[class='on']")
        if not category_name:
            raise exceptions.NoSuchElementException("没有找到选中的教师方向")

        return category_name[0]

    def get_random_teacher(self):
        """
        随机获取当前页面教师列表中的教师

        :return:
        """

        teachers = self.driver.find_elements_by_css_selector("ul.teacher-list li")
        if len(teachers) == 0:
            return None
        teacher = teachers[random.randint(0, len(teachers) - 1)]

        return teacher

    def get_teacher_info(self, teacher_info):
        """
        获得教师的信息
        :param teacher_info:
        :return: 
        """

        teacher_name = teacher_info.find_element_by_css_selector("span.f18").text
        teacher_classroom = teacher_info.find_element_by_css_selector("a.goto-look")

        return teacher_name, teacher_classroom

    def act_click_random_category(self):
        """
        随机进入一个教师方向
        :return: 
        """

        category = self.get_random_teachers_category()
        category.click()

    def act_click_random_teacher(self):
        """
        随机进入一个教师详情页
        :return: 
        """

        teacher = self.get_random_teacher()
        if teacher is not None:
            teacher_classroom = self.get_teacher_info(teacher)[1]
            teacher_classroom.click()
