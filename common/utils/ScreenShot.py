import time
import os

from selenium import webdriver


class ScreenShot:
    """
    截图工具
    """

    _root_path = os.path.dirname(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

    _save_path = os.path.join(_root_path, 'report', 'screen_shot')

    _save_extension = '.png'

    _save_file_prefix = 'screen_shot_'

    _save_datetime_format = '%Y-%m-%d-%H-%M-%S_'

    @staticmethod
    def save_screen_shot(driver: webdriver.Chrome or webdriver.Firefox, title: str, save_path: str=None, sub_directory_name: str='/'):
        """
        保存截图.
        :param driver: 浏览器对象
        :param str title: 保存的标题
        :param str save_path: 保存的路径
        :return bool: 是否成功
        """
        file_name = "{prefix}{time}{title}{extension}".format(prefix=ScreenShot._save_file_prefix,
                                                              title=title,
                                                              time=time.strftime(ScreenShot._save_datetime_format),
                                                              extension=ScreenShot._save_extension)

        save_path = save_path if save_path is not None else ScreenShot._save_path

        try:
            driver.get_screenshot_as_file(os.path.join(save_path, sub_directory_name, file_name))

            return True
        except Exception:
            return False







