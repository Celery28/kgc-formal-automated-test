import requests
import hashlib
import abc


class Interface:
    """
    基础接口
    """

    __meta__ = abc.ABCMeta

    _public_params = {
        'osType': 'android',
        'osVersion': '9999.9999.9999',
        'mechanism': 'kgc',
        'version': '1.0.0',
        'muid': '',
        'source': 0,
        'custom': '',
    }

    _gateway = 'https://api.kgc.cn/services/youke'

    _name = None

    _method = 'get'

    _timeout = 5

    _params = {}

    _response = None

    def __init__(self, method: str='get', params: dict=None, timeout: int=5):
        """
        初始化API接口对象.

        :param method:
        :param params:
        :param timeout:
        """
        if method not in ['get', 'post', 'put', 'path', 'delete', 'head']:
            raise ValueError('无效的请求方式')
        self._method = method

        for key, value in params.items() or {}.items():
            if key in self._params:
                self._params[key] = value

        self._timeout = timeout

    def ios(self):
        """
        设置请求IOS的接口.

        :return:
        """
        self._public_params['osType'] = 'iPhone'

        return self

    def android(self):
        """
        设置请求ANDROID的接口.

        :return:
        """
        self._public_params['osType'] = 'android'

        return self

    def version(self, version: str='9999.9999.9999'):
        """
        设置请求的接口的版本号，默认请求最新版本的接口.

        :param version:
        :return:
        """
        self._public_params['osVersion'] = version

        return self

    def client_version(self, version: str='1.0.0'):
        """
        设置请求接口的客户端的版本号.

        :param version:
        :return:
        """
        self._public_params['version'] = version

        return self

    def mechanism(self, mechanism: str='kgc'):
        """
        设置请求的机构，默认设置为kgc.

        :param mechanism:
        :return:
        """
        self._public_params['mechanism'] = mechanism

        return self

    def muid(self, muid: str=None):
        """
        设置muid.

        :param muid:
        :return:
        """
        if muid is None:
            md5 = hashlib.md5()
            md5.update('kgc-interface-automated'.encode())
            muid = md5.hexdigest()

        self._public_params['muid'] = muid

        return self

    def no_promotion(self):
        """
        设置推广渠道为非推广，该行为为默认行为.

        :return:
        """
        self._public_params['source'] = 0

        return self

    def promotion_gdt(self):
        """
        设置推广渠道为广点通.

        :return:
        """
        self._public_params['source'] = 1

        return self

    def promotion_xm(self):
        """
        设置推广渠道为小米应用市场.

        :return:
        """
        self._public_params['source'] = 2

        return self

    def request(self):
        """
        发送http请求
        :return:
        """
        self._params['method'] = self._name

        uri = '{gateway}?{query_string}'.format(gateway=self._gateway, query_string=self._general_query_string())
        self._response = requests.request(self._method, uri, timeout=self._timeout)

        return self

    def is_ok(self):
        """
        验证是否请求成功.

        :return:
        """
        if self._response is None:
            raise TypeError('还未发送请求，无返回结果')

        return self._response.ok

    def get_content(self):
        """
        获取返回内容.

        :return:
        """
        if self._response is None:
            raise TypeError('还未发送请求，无返回结果')

        return self._response.content

    def get_json(self):
        """
        以json字符串解析返回的内容，并返回解析后的字典.

        :return:
        """
        if self._response is None:
            raise TypeError('还未发送请求，无返回结果')

        return self._response.json()

    @staticmethod
    def get(params: dict=None, timeout: int=5):
        """
        创建一个get请求的接口.

        :param params:
        :param timeout:
        :return:
        """
        return __class__('get', params, timeout)

    @staticmethod
    def post(params: dict=None, body: dict=None, timeout: int=5):
        """
        创建一个post请求的接口.

        :param params:
        :param body:
        :param timeout:
        :return:
        """
        return __class__('post', params, timeout)

    def _general_query_string(self):
        """
        生成查询字符串.

        :return:
        """
        params = {}
        params.update(self._params)
        params.update(self._public_params)

        params = {key: value for key, value in params.items() if value}
        params = ['='.join(item) for item in params.items()]
        params.sort()

        query_string = '&'.join(params)

        return '{query_string}&auth={sign_string}'.format(query_string=query_string, sign_string=self._general_sign_string(query_string))

    def _general_sign_string(self, query_string: str, sign_key: str='bdqn'):
        """
        生成签名字符串.

        :param query_string:
        :param sign_key:
        :return:
        """
        md5 = hashlib.md5()
        md5.update((query_string + sign_key).encode())

        return md5.hexdigest()
