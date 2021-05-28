from time import sleep

from 基础.automation.pageobject.Goods import Goods
from 基础.automation.pageobject.Login import Login


class ECGoods(Goods, Login):

    def init(self):
        url = 'http://192.168.1.36/ecshop/admin/privilege.php?act=login'
        Login.open(self, url)
        Login.input_username(self)
        Login.input_password(self)
        Login.login_button(self)
        Goods.into_menu(self)
        Goods.click(self)
        Goods.out(self)
        Goods.into_main(self)

    def test_addGoods(self):
        self.init()
        Goods.click_add(self)
        Goods.goods_name(self)
        Goods.goods_category(self)
        Goods.submit(self)

    def test_search_goods(self):
        self.init()
        Goods.keyword(self)
        Goods.search_button(self)

    def unsale(self):
        self.test_search_goods()
        sleep(1)
        Goods.click_yes_gif(self)


goods = ECGoods()
# goods.test_addGoods()
# goods.test_search_goods()
