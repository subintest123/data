from automation.pageobject.Login import Login

from automation.utils.Logger import Logger

logger = Logger('ECLogin').getlog()


class ECLogin(Login):

    def login(self):
        Login.open(self)
        Login.input_username(self)
        Login.input_password(self)
        Login.login_button(self)
        logger.info(f'恭喜您登录成功')


login = ECLogin()
login.login()
