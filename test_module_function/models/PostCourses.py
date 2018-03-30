import random

from . import Page

from selenium.common import exceptions


class PostCourses(Page):
    """
    岗位课列表模型
    """

    url = "http://www.kgc.dev.cn/job"

    def get_random_post_courses(self):
        """
        随机选择岗位系列课程模块.

        :return:
        """

        post_courses_list = self.driver.find_elements_by_css_selector("div.module")
        if len(post_courses_list) == 0:
            raise exceptions.NoSuchElementException("岗位课首页没有岗位模块")

        post_courses_frame = post_courses_list[random.randint(0, len(post_courses_list) - 1)]

        return post_courses_frame

    def get_random_post_course(self):
        """
        随机选择岗位课.
        :return:
        """

        pose_courses_frame = self.get_random_post_courses()
        pose_courses = pose_courses_frame.find_elements_by_css_selector("div.img-content p a")
        if len(pose_courses) == 0:
            raise exceptions.NoSuchElementException("该岗位模块下没有岗位课")

        pose_course = pose_courses[random.randint(0, len(pose_courses) - 1)]

        return pose_course

    def act_click_random_post_course(self):
        """
        进入岗位课详情页.

        :return:
        """

        self.get_random_post_course().click()
