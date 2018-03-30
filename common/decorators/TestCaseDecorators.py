from common import utils


class TestCaseDecorators:
    """
    TestCase装饰器.
    """

    @staticmethod
    def screen_shot_in_except(title):
        """
        断言失败时截图.

        :param title:
        :return:
        """
        # TODO: 现在截图无法截取整个方页，只能截取当前窗口，需要优化
        def _screen_shot_in_except(test_func):
            def __screen_shot_in_except(self, *args, **kwargs):
                try:
                    return test_func(self, *args, **kwargs)
                except AssertionError as error:
                    utils.ScreenShot.save_screen_shot(self.driver, title, sub_directory_name='failed')
                    raise error
            return __screen_shot_in_except
        return _screen_shot_in_except

    @staticmethod
    def do_not_close_browser_tab(test_func):
        """
        单个测试不关闭浏览器标签页.

        :return:
        """
        def _do_not_close_browser_tab(self, *args, **kwargs):
            self.close_browser_current_tab_on_tear_down = False
            return test_func(self, *args, **kwargs)
        return _do_not_close_browser_tab
