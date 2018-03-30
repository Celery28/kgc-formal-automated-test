import unittest

from selenium import webdriver

from common import utils


class TestCase(unittest.TestCase):
    """
    扩展基础TestCase类.
    """

    environment = 'production'
    
    run_as = 'Chrome'

    config = {}
    
    driver = None

    close_browser_current_tab_on_tear_down = True

    def __init__(self, methodName: str='runTest'):
        if not TestCase.config:
            TestCase.config = utils.Config(None, self.environment)
        unittest.TestCase.__init__(self, methodName)

    @classmethod
    def setUpClass(cls):
        """
        测试开始前执行的动作.
        
        :return: 
        """
        cls.driver = webdriver.__dict__[cls.run_as]()

    def tearDown(self):
        """
        每个测试结束时执行的动作.
        
        :return: 
        """
        utils.ScreenShot.save_screen_shot(self.driver, '用例完成自动截图', sub_directory_name='completed')

        if self.close_browser_current_tab_on_tear_down is True:
            self.driver.close()

    @classmethod
    def tearDownClass(cls):
        """
        测试全部结束时执行的动作.
        
        :return: 
        """
        cls.driver.quit()

    @classmethod
    def set_environment(cls, environment):
        """
        设置运行时环境
        :param environment: 
        :return: 
        """
        cls.environment = environment
