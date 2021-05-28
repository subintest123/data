from time import sleep
from automation.pageobject.Goods import Goods
from automation.pageobject.Login import Login


class ECGoods(Goods, Login):

    def init(self):
        url = 'http://192.168.1.36/ecshop/admin/privilege.php?act=login'
        Login.open(self, url)
        Login.input_username(self)
        Login.input_password(self)
        Login.login_button(self)
        Goods.into_one_frame(self)
        Goods.click_list(self)
        Goods.out_frame(self)
        Goods.into_next_frame(self)

    def test_add_goods(self):
        self.init()
        Goods.click_add(self)
        Goods.goods_name(self)
        Goods.goods_category(self)
        Goods.submit(self)

    def test_search_goods(self):
        self.init()
        Goods.keyword(self)
        Goods.search_button(self)

    def is_on_sale(self):
        self.test_search_goods()
        sleep(1)
        Goods.click_yes_gif(self)


goods = ECGoods()
goods.test_add_goods()
# goods.test_search_goods()
# goods.is_on_sale()
