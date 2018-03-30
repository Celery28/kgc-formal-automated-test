import models


class CourseTag(models.Page):
    """
    课程标签详情页模型.
    """

    def get_categories(self)->list:
        """
        获取分类列表.
        
        :return: 
        """
        return self.driver.find_elements_by_css_selector("div.list_box ul li a")

    def get_course_list(self)->list:
        """
        获取课程列表.
        
        :return: 
        """
        return self.driver.find_elements_by_css_selector("li.course_detail")

    def act_switch_to_teacher_tab(self)->None:
        """
        切换标签页到相关讲师.
        
        :return: 
        """
        teacher = self.driver.find_element_by_link_text("相关讲师")
        self.action_chains.move_to_element(teacher).perform()
