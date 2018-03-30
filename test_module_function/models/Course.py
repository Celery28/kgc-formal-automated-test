import random

from . import Page

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class Course(Page):
    """
    课程页面模型
    """

    def get_course_name(self)->str:
        """
        获取课程名称.

        :return str:
        """
        title = self.driver.find_element_by_css_selector('div#title h2')

        return title.text

    def get_course_price(self)->int:
        """
        获取课程价格.

        :return int:
        """

        price = self.driver.find_element_by_css_selector('span.price_zh')

        if '免费' == price.text:
            return 0

        return int(price.text.ltrim('￥'))

    def get_course_original_price(self)->int or None:
        """
        获取课程原价.

        :return int or None:
        """
        try:
            price = self.driver.find_element_by_css_selector('span.product-detail-old')

            return int(price.text)
        except exceptions.NoSuchElementException:
            return None

    def get_buy_button(self)->WebElement or None:
        """
        获取购买按钮.

        :return None or WebElement:
        """
        try:
            button = self.driver.find_element_by_css_selector('div.view-buy-btn a#open')
        except exceptions.NoSuchElementException:
            return None

        return button

    def is_allow_buy(self)->bool:
        """
        判断该课程是否允许购买.

        :return bool:
        """
        return True if self.get_buy_button() is not None else False

    def is_allow_buy_on_k_coins(self)->bool:
        """
        检查是否允许使用kb购买，该方法应该在点击购买按钮弹出支付方式选择窗口之后调用.

        :return bool:
        """

        try:
            self.driver.find_element_by_css_selector('div.pay_type p.kgcpay')
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_buy_success(self)->bool:
        """
        是否购买成功.

        :return bool:
        """
        self.driver.implicitly_wait(10)

        is_success = False
        try:
            self.driver.find_element_by_css_selector('a.project-back').click()
            is_success = True
        except exceptions.NoSuchElementException:
            try:
                self.driver.find_element_by_css_selector('div.view-buy-btn a.catalog-btn')
                is_success = True
            except exceptions.NoSuchElementException:
                pass

        self.driver.implicitly_wait(3)
        return is_success

    def is_favorite_for_course(self)->bool:
        """
        检查是否已经关注.

        :return str:
        """
        try:
            self.driver.find_element_by_css_selector('a.cancelFavorite')
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_un_favorite_for_course(self)->bool:
        """
        检查是否未关注
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a#favorites')
            return True
        except exceptions.NoSuchElementException:
            return False

    def get_tags(self)->list:
        """
        获取课程标签列表.
        
        :return: 
        """
        return self.driver.find_elements_by_css_selector("div.biaoqian a")

    def get_random_tag(self)->WebElement or None:
        """
        随机获取一个标签.
        
        :return: 
        """
        tags = self.get_tags()

        if 0 == len(tags):
            return None

        return tags[random.randint(0, len(tags) - 1)]

    def get_teacher_name(self)->str:
        """
        获取教师名称.
        
        :return: 
        """
        return self.driver.find_element_by_css_selector("a.course-teacher-link").text

    def is_vote_for_teacher(self)->bool:
        """
        判断是否已经对教师点赞.
        
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teacher-zan-on')
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_favorite_for_teacher(self)->bool:
        """
        判断是否已经关注教师.
        
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teach-has-sc')
            return True
        except exceptions.NoSuchElementException:
            return False

    def is_un_favorite_for_teacher(self)->bool:
        """
        检查是否未关注教师.
        
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('a.teach-no-sc')
            return True
        except exceptions.NoSuchElementException:
            return False

    def has_tag(self)->bool:
        """
        检查课程是否拥有标签.
        
        :return: 
        """
        tags = self.get_tags()

        return True if 0 < len(tags) else False

    def act_click_favorite(self)->None:
        """
        点击关注按钮.

        :return void:
        """
        try:
            self.driver.find_element_by_css_selector('a#favorites').click()
        except exceptions.NoSuchElementException:
            pass

    def act_click_cancel_favorite(self)->None:
        """
        点击取消关注按钮.
        
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector('div.pro_share a.cancelFavorite').click()
        except exceptions.NoSuchElementException:
            pass

    def act_click_share_qq(self)->None:
        """
        点击qq分享按钮.

        :return void:
        """
        self.driver.find_element_by_css_selector('a.product-share-qq-btn').click()

    def act_click_share_wb(self)->None:
        """
        点击微博分享按钮.

        :return void:
        """

        self.driver.find_element_by_css_selector('a.product-share-wb-btn').click()

    def act_click_share_wx(self)->None:
        """
        点击微信分享按钮.

        :return void:
        """

        self.driver.find_element_by_css_selector('a.product-share-wx-btn').click()

    def act_click_buy_button(self)->None:
        """
        点击购买按钮.

        :return void:
        """
        button = self.get_buy_button()

        if button is None:
            raise exceptions.NoSuchElementException('没有找到购买按钮')

        button.click()

    def act_select_k_coins_pay_method(self)->None:
        """
        选择kb支付方式.

        :return void:
        """
        self.driver.find_element_by_css_selector('div.pay_type p.kgcpay').click()

    def act_click_confirm_buy(self)->None:
        """
        点击确认购买.

        :return void:
        """

        self.driver.find_element_by_css_selector('a#confirm-buy-button').click()

    def act_click_vote_for_teacher(self)->None:
        """
        对教师点赞.
        
        :return: 
        """
        self.driver.find_element_by_css_selector("a.teacher-zan").click()

    def act_click_favorite_for_teacher(self)->None:
        """
        点击关注教师/取消关注教师按钮.
        
        :return: 
        """
        self.driver.find_element_by_css_selector("a.teach-sc").click()

    def act_switch_to_comment_tab(self)->None:
        """
        切换到课程评价标签页.
        
        :return: 
        """
        self.driver.find_element_by_css_selector("a#coursed-pj-tab").click()

    def act_switch_to_ask_tab(self)->None:
        """
        切换到问答标签页.
        
        :return: 
        """
        self.driver.find_element_by_css_selector("a#coursed-ask-tab").click()

    def act_click_random_tag(self)->None:
        """
        随机点击一个课程标签.
        
        :return: 
        """
        tag = self.get_random_tag()

        if isinstance(tag, WebElement):
            tag.click()

    def act_click_teacher_name(self)->None:
        """
        点击教师名称进入详情页.
        
        :return: 
        """
        self.driver.find_element_by_css_selector("a.course-teacher-link").click()

    def act_select_of_grade_5(self)->None:
        """
        选择5颗星的评价等级.
        
        :return: 
        """
        self.driver.find_element_by_css_selector("div#open_grade_4 ").click()

    def act_commit_course_comment(self, comment: str)->None:
        """
        添加课程评价
        :param comment: 
        :return: 
        """
        self.act_select_of_grade_5()
        self.driver.find_element_by_css_selector("#KgcOpenComment_comment_content").send_keys(comment)
        self.driver.find_element_by_css_selector("#postComment").click()
