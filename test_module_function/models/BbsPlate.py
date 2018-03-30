from . import Page


class BbsPlate(Page):
    """
    微社区板块详情页
    """

    def get_plate_name(self):
        """
        获取板块名称
        :return:
        """

        return self.driver.find_element_by_css_selector("h2.discuz-name")
