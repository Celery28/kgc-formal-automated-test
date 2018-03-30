import unittest
import abc

"""
基础测试套件

:author: ronghui.huo <ronghui.huo@kgc.cn>
"""


class TestSuite(unittest.TestSuite):
    """
    扩展unittest的TestSuite，增加自定义的测试套件
    """

    __mate__ = abc.ABCMeta

    def __init__(self, tests=()):
        unittest.TestSuite.__init__(self, tests)
        self.suites()

    @abc.abstractmethod
    def suites(self):
        """
        所有的子类应该实现该方法以添加自定义的测试套件.

        :return:
        """
        pass
