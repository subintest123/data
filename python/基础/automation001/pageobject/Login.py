from automation.base.BasePage import BasePage


class Login(BasePage):

    def input_username(self):
        BasePage.input_by_name(self, 'username', 'caichang')

    def input_password(self):
        BasePage.input_by_name(self, 'password', 'caichang1')
