from . import Page


class Login(Page):
    """
    登录页面模型
    """

    def act_login(self, username: str, password: str)->None:
        """
        登录动作
        :param username:
        :param password:
        :return:
        """
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('KgcForm_models_LoginForm_identity').send_keys(username)
        self.driver.find_element_by_id('KgcForm_models_LoginForm_password').send_keys(password)
        self.driver.find_element_by_id('login').click()
