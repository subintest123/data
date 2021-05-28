from automation.pageobject.Login import Login


class ECLogin(Login):

    def login(self):
        url = 'http://192.168.1.36/ecshop/admin/privilege.php?act=login'
        Login.open(self, url)
        Login.max_browser(self)



login = ECLogin()
login.login()
