import random

from . import Page

from selenium.common import exceptions


class SeriesCourse(Page):
    """
    系列课集合页模型
    """
    def get_random_series_course(self):
        """
        获取课程数量,并随机获得一节系列课
        :return:
        """

        series_courses = self.driver.find_elements_by_css_selector("#catalog-list li")
        if len(series_courses) == 0:
            raise exceptions.NoSuchElementException("该系列课下没有课程，快去联系业务老师提bug吧")
        series_courses_len = len(series_courses)
        series_course = series_courses[random.randint(0, len(series_courses) - 1)]

        return series_courses_len, series_course

    def get_series_course_message(self, series_course):
        """
        获取系列课信息
        :param series_course:
        :return:
        """
        course_name = series_course.find_element_by_css_selector("div.catalogList_con a")
        course_buy_number = series_course.find_element_by_css_selector("h1.buyNumer i")
        course_img = series_course.find_element_by_css_selector("div.catalogList_img a")

        return course_name, course_buy_number, course_img

    def get_series_course_number(self):
        """
        获取系列课课程节数
        :return:
        """

        series_course_number = self.driver.find_element_by_css_selector("div.seriesH_con h2 span")

        return series_course_number
