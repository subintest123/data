from 基础.automation.base.BasePage import BasePage


class Goods(BasePage):
    def into_menu(self):
        BasePage.into_frame(self, 'menu-frame')

    def out(self):
        BasePage.out_frame(self)

    def click(self):
        BasePage.click(self, 'link_text=>商品列表')

    def into_main(self):
        BasePage.into_frame(self, 'main-frame')

    def click_add(self):
        BasePage.click(self, 'xpath=>/html/body/h1/span[1]/a')

    def goods_name(self):
        BasePage.input(self, 'name=>goods_name', '凤姐你好')

    def goods_category(self):
        BasePage.select_by_text(self, 'name=>cat_id', '智能硬件')

    def submit(self):
        BasePage.click(self, 'xpath=>//input[@value=" 确定 "]')

    def keyword(self):
        BasePage.input(self, 'name=>keyword', '尧海王')

    def search_button(self):
        BasePage.click(self, 'xpath=>//input[@value=" 搜索 "]')

    def click_yes_gif(self):
        BasePage.click(self, 'xpath=>//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img')

    def get_images(self):
        images = BasePage.get_goods_isonsale_ico(self, 'xpath=>//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img',
                                                 'src')
        return images
