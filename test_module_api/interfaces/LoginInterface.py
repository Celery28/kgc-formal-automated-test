from . import Interface


class LoginInterface(Interface):
    """
    登录接口.
    """

    _name = 'login'

    _params = {
        'passport': None,
        'password': None,
    }
