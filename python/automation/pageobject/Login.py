from automation.base.BasePage import BasePage
from automation.utils.Logger import Logger

# 获得日志
logger = Logger('Login').getlog()


class Login(BasePage):

    def input_username(self):
        # 查找‘name’元素为‘username’，并输入‘caichang’
        BasePage.input(self, 'name=>username', 'caichang')

    def input_password(self):
        # 查找‘name’元素为‘password’，并输入‘caichang1’
        BasePage.input(self, 'name=>password', 'caichang1')

    def login_button(self):
        # 查找‘class_name’元素为‘btn-a’，并点击
        BasePage.click(self, 'class_name=>btn-a')
        logger.info(f'您点击了登录')
