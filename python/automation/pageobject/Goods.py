from automation.base.BasePage import BasePage
from automation.utils.Logger import Logger

logger = Logger('Goods').getlog()


class Goods(BasePage):

    # 进入内帧
    def into_one_frame(self):
        BasePage.into_frame(self, 'menu-frame')

    # 退出内帧
    def out_frame(self):
        BasePage.out_frame(self)

    # 点击...元素
    def click_list(self):
        BasePage.click(self, 'link_text=>商品列表')

    # 进入另一个内帧
    def into_next_frame(self):
        BasePage.into_frame(self, 'main-frame')

    # 点击创建
    def click_add(self):
        BasePage.click(self, 'xpath=>/html/body/h1/span[1]/a')
        logger.info(f'您点击了添加商品')

    # 商品的名称
    def goods_name(self):
        BasePage.input(self, 'name=>goods_name', '灞波儿奔')
        logger.info(f'您输入了新的商品名')

    # 定义商品的分类
    def goods_category(self):
        BasePage.select_by_text(self, 'name=>cat_id', '手机')

    # 点击确定
    def submit(self):
        BasePage.click(self, 'xpath=>//input[@value=" 确定 "]')

    # 输入搜索关键字
    def keyword(self):
        BasePage.input(self, 'name=>keyword', '灞')

    # 点击搜索
    def search_button(self):
        BasePage.click(self, 'xpath=>//input[@value=" 搜索 "]')

    # 点击进行上、下架
    def click_yes_gif(self):
        BasePage.click(self, 'xpath=>//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img')

    # 获得上架/下架操作的按钮图标
    def get_images(self):
        images = BasePage.get_goods_isonsale(self, 'xpath=>//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img',
                                             'src')
        return images
