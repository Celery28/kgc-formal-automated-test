from . import TestSuite

from test_module_api import testcases


class AccountTestSuite(TestSuite):

    def suites(self):
        self.addTest(testcases.LoginTestCase('test_login_on_success'))
