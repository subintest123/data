import unittest
from automation.pageobject.Login import Login
from automation.utils.Logger import Logger

logger = Logger('Testlogin').getlog()


class Testlogin(unittest.TestCase, Login):

    # 执行下面的用例之前，先打开链接
    def setUp(self):
        Login.open(self)

    # 登录
    def test_login(self):
        Login.input_username(self)
        Login.input_password(self)
        logger.info(f'您点击了登录按钮')
        Login.login_button(self)

    # 执行用例之后，关闭打开的浏览器
    def tearDown(self):
        Login.close_bowser(self)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
