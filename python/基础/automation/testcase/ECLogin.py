from automation.pageobject.Login import Login
from automation.utils.Logger import Logger

logger = Logger('ECLogin').getlog()
class ECLogin(Login):

    def login(self):
        Login.open(self)
        Login.input_username(self)
        Login.input_password(self)
        logger.info('你点击了登录按钮')
        Login.login_button(self)


login = ECLogin()
login.login()
