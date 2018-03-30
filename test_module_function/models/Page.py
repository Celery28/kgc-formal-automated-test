from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.webdriver.support import wait


class Page:
    """
    页面基础类
    """

    url = None

    current_handle = None

    _action_chains = None

    def __init__(self, driver: webdriver.Chrome or webdriver.Firefox, url: str=None):
        """
        初始化页面
        :param driver:
        :param url:
        """
        self.driver = driver
        self.driver.implicitly_wait(3)

        if url is not None or self.url is not None:
            self.driver.get(url if url is not None else self.url)

        try:
            self.driver.maximize_window()
        except exceptions.WebDriverException:
            pass
        self.current_handle = self.driver.current_window_handle
        handlers = self.driver.window_handles
        self.driver.switch_to.window(handlers[-1])

    @property
    def action_chains(self)->ActionChains:
        """
        只读属性，该属性为ActionChains类的实例
        :return ActionChains: 
        """

        self._action_chains = ActionChains(self.driver)

        return self._action_chains

    def get_current_page_url(self)->str:
        """
        获取当前页面url.

        :return str:
        """

        return self.driver.current_url

    def get_current_window_handle(self)->str:
        """
        获取当前窗口的操作句柄.

        :return str:
        """

        return self.driver.current_window_handle

    def act_switch_to_self_handle(self)->None:
        """
        切换窗口句柄到当前页面.
        
        :return:
        """
        self.driver.switch_to.window(self.current_handle)

    def refresh(self):
        """
        刷新页面.

        :return:
        """
        self.driver.refresh()

    def act_switch_to_last_window(self):
        """
        切换窗口句柄到最后一个窗口.
        
        :return: 
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def act_close_sign_tip(self)->None:
        """
        点击关闭签到按钮.
        
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector("a.header-qd-close").click()
        except exceptions.NoSuchElementException:
            pass

    def act_close_dialog(self)->None:
        """
        关闭消息弹窗.
        
        :return: 
        """
        try:
            self.driver.find_element_by_css_selector("a.dialog-close-button").click()
        except Exception:
            pass

    def set_window_scroll_position(self, x: int, y: int)->None:
        """
        设置浏览器滚动条位置
        
        :param int x: 
        :param int y: 
        :return: 
        """

        scroll_top = int(self.driver.execute_script('return document.documentElement.scrollTop'))
        self.driver.execute_script('document.documentElement.scrollLeft={0};'.format(x))
        self.driver.execute_script('document.documentElement.scrollTop={0};'.format(y + scroll_top))

    def close(self)->None:
        """
        关闭当前页面.
        
        :return: 
        """
        self.driver.close()

    def wait(self, until, timeout: int=30, interval: float or int=0.5):
        """
        显示的等待页面加载并检查页面元素
        :param until:
        :param timeout:
        :param interval:
        :return:
        """
        return wait.WebDriverWait(self.driver, timeout=timeout, poll_frequency=interval).until(until)
