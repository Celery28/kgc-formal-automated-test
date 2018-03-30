from . import Page


class Homepage(Page):
    """
    课工场网站首页模型
    """

    url = "http://www.kgc.dev.cn"

    def act_courses(self):
        """
        进入课程库
        :return:
        """
        courses = self.driver.find_element_by_css_selector("span.nav-all-c a")
        courses.click()

    def act_employment_base(self):
        """
        进入就业实训基地
        :return:
        """

        employment_base = self.driver.find_element_by_css_selector("img.top5")
        employment_base.click()

    def act_job(self):
        """
        进入岗位课界面
        :return:
        """

        job = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div[3]/div/div/div/div/a")
        job.click()

    def act_teachers(self):
        """
        进入金牌讲师界面
        :return:
        """

        more_button = self.driver.find_element_by_css_selector("div.good-teacher span.title-r a")
        more_button.click()
