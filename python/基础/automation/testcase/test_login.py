import unittest

from automation.pageobject.Login import Login
from automation.utils.Logger import Logger

logger = Logger('ECLogin').getlog()


@unittest.skip('cc')
class TestLogin(unittest.TestCase,Login):
    def setUp(self):
        Login.open(self)

    def test_login(self):
        Login.input_username(self)
        Login.input_password(self)
        logger.info('你点击了登录按钮')
        Login.login_button(self)

    def tearDown(self):
        Login.close_browser(self)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
