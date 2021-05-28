from automation.base.BasePage import BasePage
from automation.utils.Logger import Logger

logger = Logger('Login').getlog()
class Login(BasePage):

    def input_username(self):
        logger.info('你往name属性为username的框中写入了caichang值')
        BasePage.input(self,'name=>username','caichang')

    def input_password(self):
        BasePage.input(self,'name=>password','caichang1')

    def login_button(self):
        BasePage.click(self,'class_name=>btn-a')
