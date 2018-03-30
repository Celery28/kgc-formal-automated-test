from . import Page
import random, time
from selenium.common import exceptions


class PostCourse(Page):
    """
    岗位课详情页.
    """

    def get_next_course(self):
        """
        获取下一课的状态.

        :return:
        """
        try:
            next_course = self.driver.find_element_by_css_selector("div.nextCourse span")
            return next_course
        except exceptions.NoSuchElementException:
            return None

    def get_next_course_name(self):
        """
        获取下一课的名称.

        :return:
        """
        try:
            next_course_name = self.driver.find_element_by_css_selector("div.nextCourse p")
            return next_course_name
        except exceptions.NoSuchElementException:
            return None

    def has_next_course(self):
        """
        验证是否有下一课.
        
        :return: 
        """
        next_course = self.get_next_course()

        return False if next_course is None else True

    def act_click_next_course(self):
        """
        点击进入下一课

        :return:
        """

        next_course = self.get_next_course()
        if next_course is None:
            raise exceptions.NoSuchElementException("该岗位课没有下一课")
        else:
            next_course.click()

    def get_random_post_courses_course_chapters(self):
        """
        随机获取某个课程章节
        :return:
        """

        course_chapters = self.driver.find_elements_by_css_selector("ul.common-learn-line li")
        if len(course_chapters) == 0:
            raise exceptions.NoSuchElementException("该岗位课下没有章节，请联系业务老师进行处理")

        chapter = course_chapters[random.randint(0, len(course_chapters) - 1)]
        button = chapter.find_element_by_css_selector("i.head-tb")
        if -1 == button.get_attribute('class').find('learn-show'):
            button.click()

        return chapter

    def get_chapter_title(self, chapter):
        """
        获取章节标题
        :param chapter:
        :return:
        """
        return chapter.find_element_by_css_selector("strong.h2").text

    def get_random_post_courses_course_details_page(self, course_chapter):
        """
        从岗位课中随机获取某个课程
        :return:
        """

        courses = course_chapter.find_elements_by_css_selector("dl.list-course-box dt")
        if len(courses) == 0:
            raise exceptions.NoSuchElementException("该章节下没有课程，请联系业务老师进行处理")
        course = courses[random.randint(0, len(courses) - 1)]

        return course

    def get_course_message(self, course):
        """
        获取随机获取的课程信息
        :return:
        """

        course_name = course.find_element_by_css_selector("a.course-name")
        course_know = course.find_element_by_css_selector("a.know-course").get_attribute("href")

        return course_name, course_know

    def act_click_course(self, course):
        """
        点击课程进入课程详情页
        :param course:
        :return:
        """
        course_name = course.find_element_by_css_selector("a.course-name")
        self.action_chains.move_to_element(course_name).perform()
        time.sleep(1)
        course.find_element_by_css_selector("a.know-course").click()

        return True





