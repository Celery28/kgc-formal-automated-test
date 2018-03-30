import random

from . import Page

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class Courses(Page):
    """
    课程库列表页模型
    """
    url = 'http://www.kgc.cn/list'

    title_link_css_selector = 'a.course-title-a'

    def get_current_title(self)->str:
        """
        获取当前页面的title标签值
        :return str:
        """

        return self.driver.title

    def get_random_first_category(self)->WebElement:
        """
        随机获取课程方向
        :return:
        """

        first_categories = self.driver.find_elements_by_xpath('//*[@id="leftContent"]/dl/dd[1]/div/a')

        if 0 == len(first_categories):
            raise exceptions.NoSuchElementException('没有找到任何课程方向')

        first_category = first_categories[random.randint(1, len(first_categories) - 1)]

        return first_category

    def get_current_first_category(self)->WebElement:
        """
        获取当前选中的课程方向
        :return:
        """
        category = self.driver.find_elements_by_xpath('//*[@id="leftContent"]/dl/dd[1]/div/a[@class="on"]')

        if not category:
            raise exceptions.NoSuchElementException('没有找到被选中的课程方向')

        return category[0]
    
    def get_random_sub_category(self)->WebElement:
        """
        随机获取课程分类
        :return:
        """

        sub_categories = self.driver.find_elements_by_xpath('//*[@id="leftContent"]/dl/dd[2]/div/a')

        if 0 == len(sub_categories):
            raise exceptions.NoSuchElementException('没有找到任何课程分类')

        sub_category = sub_categories[random.randint(1, len(sub_categories) - 1)]
        
        return sub_category

    def get_current_sub_category(self)->WebElement:
        """
        获取当前选中的课程分类
        :return: 
        """
        category = self.driver.find_elements_by_xpath('//*[@id="leftContent"]/dl/dd[2]/div/a[@class="on"]')

        if not category:
            raise exceptions.NoSuchElementException('没有找到被选中的课程分类')

        return category[0]
    
    def get_random_courses_page_url(self)->str or None:
        """
        随机获取一个课程列表页的链接
        :return:
        """

        pages = self.driver.find_elements_by_css_selector('div.pager ul a')

        if len(pages) > 0:
            current_url = self.driver.current_url
            url_parse_list = current_url.split('-')
            last_page = pages[-2]
            page = random.randint(1, int(last_page.text))
            url_parse_list[1] = str(page)
            url = '-'.join(url_parse_list)
            
            return url
        
        return None

    def get_current_page_courses(self)->list:
        """
        获取当前列表的所有课程.

        :return WebElement[]:
        """
        courses = self.driver.find_elements_by_xpath('//*[@id="yw1"]/ul/li')

        return courses

    def get_free_courses(self)->list:
        """
        筛选免费课程

        :return:
        """
        self.act_switch_price_filter_to_free()
        courses = self.get_current_page_courses()

        return courses

    def get_no_free_courses(self)->list:
        """
        筛选收费课程

        :return:
        """

        self.act_switch_price_filter_to_no_free()
        courses = self.get_current_page_courses()

        return courses

    def get_current_page_course_count(self)->int:
        """
        获取当前列表页课程数量.

        :return int:
        """
        courses = self.get_current_page_courses()

        return len(courses)
    
    def get_random_course(self)->WebElement:
        """
        随机获取课程
        :return WebElement:
        """

        courses = self.get_current_page_courses()
        if 0 == len(courses):
            raise exceptions.NoSuchElementException('没有找到任何课程')

        get_course = courses[random.randint(0, len(courses)-1)]

        return get_course

    def get_random_no_free_course(self)->WebElement or None:
        """
        随机获取一个收费课程.

        :return:
        """

        courses = self.get_current_page_courses()
        no_free_courses = []

        self.driver.implicitly_wait(0)
        for course in courses:
            try:
                price = course.find_element_by_css_selector('span.view0-price')
            except exceptions.NoSuchElementException:
                price = course.find_element_by_css_selector('span.view0-old')

            if '免费' != price.text:
                no_free_courses.append(course)
        self.driver.implicitly_wait(3)

        if 0 == len(no_free_courses):
            return None

        course = no_free_courses[random.randint(0, len(no_free_courses) - 1)]

        return course

    def get_random_free_course(self)->WebElement or None:
        """
        随机获取一个免费课程.
        :return:
        """

        courses = self.get_free_courses()

        free_courses = []
        self.driver.implicitly_wait(0)
        for course in courses:
            try:
                price = course.find_element_by_css_selector('span.view0-price')
            except exceptions.NoSuchElementException:
                price = course.find_element_by_css_selector('span.view0-old')

            if '免费' == price.text:
                free_courses.append(course)
        self.driver.implicitly_wait(3)

        if 0 == len(free_courses):
            return None

        course = free_courses[random.randint(0, len(free_courses) - 1)]

        return course

    def get_random_live_course(self, status=1)->WebElement or None:
        """
        随机获取一个直播课程.

        :param int status: 直播课状态：1为即将直播；2为正在直播；其他为直播结束
        :return:
        """

        courses = self.get_current_page_courses()

        live_courses = []
        self.driver.implicitly_wait(0)
        for course in courses:
            try:
                if 1 == status:
                    live_class_name = 'liveSoon'
                elif 2 == status:
                    # TODO:需要获取到正在直播的类名称
                    live_class_name = 'liveSoon'
                else:
                    live_class_name = 'liveEnd'
                course.find_element_by_css_selector('div.{0}'.format(live_class_name))
            except exceptions.NoSuchElementException:
                continue
            else:
                live_courses.append(course)
        self.driver.implicitly_wait(3)

        if 0 == len(live_courses):
            return None

        course = live_courses[random.randint(0, len(live_courses) - 1)]

        return course

    def get_current_courses_sort(self):
        """
        获取课程的排序条件.
        
        :return: 
        """

        courses_sort = self.driver.find_element_by_css_selector("div.list-top-left label")

        return courses_sort

    def get_current_courses_price_filter(self):
        """
        获取课程价格状态.

        :return:
        """

        price = self.driver.find_element_by_css_selector("div.list-top-mld label")

        return price

    def get_current_courses_difficulty_level_filter(self):
        """
        获取课程库列表的课程难度等级.
        
        :return: 
        """
        return self.driver.find_element_by_css_selector("div.list-top-right label")

    def act_click_random_first_category(self)->None:
        """
        随机进入一个课程方向页.

        :return void:
        """
        first_category = self.get_random_first_category()
        first_category.click()

    def act_click_random_sub_category(self)->None:
        """
        随机进入一个课程分类页.

        :return void:
        """
        sub_category = self.get_random_sub_category()
        sub_category.click()

    def act_click_random_courses_page_url(self)->None:
        """
        随机进入一个课程列表页.

        :return void:
        """
        url = self.get_random_courses_page_url()

        if url is not None:
            self.driver.get(url)

    def act_click_random_course(self)->None:
        """
        随机进入一个课程详情页.

        :return void:
        """
        course = self.get_random_course()
        self.set_window_scroll_position(**course.location_once_scrolled_into_view)
        course.find_element_by_css_selector(self.title_link_css_selector).click()

    def act_click_random_no_free_course(self)->None:
        """
        随机进入一个收费课程详情页.

        :return void:
        """

        course = self.get_random_no_free_course()
        if course is None:
            raise exceptions.NoSuchElementException("在当前列表页没有找到收费的课程")

        self.set_window_scroll_position(**course.location_once_scrolled_into_view)
        course.find_element_by_css_selector(self.title_link_css_selector).click()

    def act_click_random_free_course(self)->None:
        """
        随机进入一个免费课程详情页.

        :return void:
        """

        course = self.get_random_free_course()
        if course is None:
            raise exceptions.NoSuchElementException("在当前列表页没有找到免费的课程")

        self.set_window_scroll_position(**course.location_once_scrolled_into_view)
        course.find_element_by_css_selector(self.title_link_css_selector).click()

    def act_click_live_course(self, status: int=1)->None:
        """
        随机进入一个直播课程详情页.

        :param status:
        :return void:
        """
        course = self.get_random_live_course(status)
        if course is None:
            raise exceptions.NoSuchElementException("在当前列表页没有找到符合条件的直播课程")

        self.set_window_scroll_position(**course.location_once_scrolled_into_view)
        course.find_element_by_css_selector(self.title_link_css_selector).click()

    def act_switch_courses_sort_to_hot(self)->None:
        """
        切换当前排序选项为最热.
        
        :return: 
        """

        sort = self.get_current_courses_sort()
        if sort.text != '最热':
            self.action_chains.move_to_element(sort).perform()
            self.driver.find_element_by_link_text('最热').click()

    def act_switch_courses_sort_to_new(self)->None:
        """
        切换当前排序选项为最新.
        
        :return: 
        """

        sort = self.get_current_courses_sort()
        if sort.text != '最新':
            self.action_chains.move_to_element(sort).perform()
            self.driver.find_element_by_link_text('最新').click()

    def act_switch_price_filter_to_free(self)->None:
        """
        切换当前的价格过滤器到免费课程.
        
        :return: 
        """

        price = self.get_current_courses_price_filter()
        position = price.location_once_scrolled_into_view
        self.set_window_scroll_position(position['x'], position['y'] - 100)

        if price.text != "免费":
            self.action_chains.move_to_element(price).perform()
            self.driver.find_element_by_link_text('免费').click()

    def act_switch_price_filter_to_no_free(self)->None:
        """
        切换当前的价格过滤器到收费课程.
        
        :return: 
        """

        price = self.get_current_courses_price_filter()
        position = price.location_once_scrolled_into_view
        self.set_window_scroll_position(position['x'], position['y'] - 100)

        if price.text != '付费':
            self.action_chains.move_to_element(price).perform()
            self.driver.find_element_by_link_text('付费').click()

    def act_switch_courses_difficulty_level_to_zero_based(self) -> None:
        """
        切换当前的难度等级到零基础.

        :return:
        """

        difficulty_level = self.get_current_courses_difficulty_level_filter()

        if '零基础' != difficulty_level.text:
            self.action_chains.move_to_element(difficulty_level).perform()
            self.driver.find_element_by_link_text('零基础').click()

    def act_switch_courses_difficulty_level_to_based(self) -> None:
        """
        切换当前的难度等级到基础.

        :return:
        """

        difficulty_level = self.get_current_courses_difficulty_level_filter()

        if '基础' != difficulty_level.text:
            self.action_chains.move_to_element(difficulty_level).perform()
            self.driver.find_element_by_link_text('基础').click()

    def act_switch_courses_difficulty_level_to_middle_level(self) -> None:
        """
        切换当前的难度等级到中级.

        :return:
        """

        difficulty_level = self.get_current_courses_difficulty_level_filter()

        if '中级' != difficulty_level.text:
            self.action_chains.move_to_element(difficulty_level).perform()
            self.driver.find_element_by_link_text('中级').click()

    def act_switch_courses_difficulty_level_to_high_level(self) -> None:
        """
        切换当前的难度等级到高级.

        :return:
        """

        difficulty_level = self.get_current_courses_difficulty_level_filter()

        if '高级' != difficulty_level.text:
            self.action_chains.move_to_element(difficulty_level).perform()
            self.driver.find_element_by_link_text('高级').click()

    def act_switch_courses_difficulty_level_to_all_level(self) -> None:
        """
        切换当前的难度等级到全部.

        :return:
        """

        difficulty_level = self.get_current_courses_difficulty_level_filter()

        if '全部' != difficulty_level.text:
            self.action_chains.move_to_element(difficulty_level).perform()
            self.driver.find_element_by_link_text('全部').click()

