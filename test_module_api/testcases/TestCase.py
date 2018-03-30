import unittest

from common import utils


class TestCase(unittest.TestCase):
    """
    扩展基础TestCase类.
    """

    environment = 'production'

    config = {}

    def __init__(self, methodName: str='runTest'):
        if not TestCase.config:
            TestCase.config = utils.Config(None, self.environment)
        unittest.TestCase.__init__(self, methodName)

    @classmethod
    def set_environment(cls, environment):
        """
        设置运行时环境
        :param environment: 
        :return: 
        """
        cls.environment = environment
