from . import TestCase

from test_module_api import interfaces


class LoginTestCase(TestCase):
    
    def setUp(self):
        pass
    
    def test_login_on_success(self):
        api = interfaces.LoginInterface.get({'passport': '18310432052', 'password': '654321'})
        api.request()
        
        self.assertTrue(api.is_ok(), '请求失败')
        self.assertIsInstance(api.get_json(), dict, '返回的数据错误')
    
    def tearDown(self):
        pass
