import unittest
from time import sleep

from automation.dao.MysqlHelper import MySQLHelper
from automation.pageobject.Goods import Goods
from automation.pageobject.Login import Login
from automation.utils.Logger import Logger

logger = Logger('Testgoods').getlog()


class Testgoods(unittest.TestCase, Goods, Login):

    @classmethod
    # 整个类开始前，先打开数据库链接
    def setUpClass(cls):
        cls.data = MySQLHelper()

    # 以下用例执行前登录并进入内帧
    def setUp(self):
        Login.open(self)
        Login.input_username(self)
        Login.input_password(self)
        Login.login_button(self)
        Goods.into_one_frame(self)
        Goods.click_list(self)
        Goods.out_frame(self)
        Goods.into_next_frame(self)

    @unittest.skip
    # 添加商品
    def test_addGoods(self):
        Goods.click_add(self)
        Goods.goods_name(self)
        Goods.goods_category(self)
        Goods.submit(self)

    @unittest.skip
    # 查询商品
    def test_search_goods(self):
        Goods.keyword(self)
        Goods.search_button(self)

    # 上、下架商品
    def test_unsale(self):
        Goods.keyword(self)
        Goods.search_button(self)
        sleep(1)

        sleep(1)
        src_property = Goods.get_images(self)
        logger.info(src_property)

        if src_property == 'yes.gif':
            src_property = 1  # 1为上架
        else:
            src_property = 0  # 0为下架

        # 查询ecs_goods表中带‘灞’字的商品的名字，和上下架状态
        query = "select goods_name,is_on_sale from ecs_goods where goods_name like '%灞%'"
        result = self.data.select(query, 'one')

        if result[1] == src_property:
            Goods.click_yes_gif(self)
            logger.info(result[1])
            sleep(2)
            sql = "select goods_name,is_on_sale from ecs_goods where goods_name like '%灞%'"
            result = self.data.select(sql, 'one')
            self.assertEqual(result[1], 0)
        else:
            logger.info('页面有变更或sql有错误')

    @classmethod
    # 整个类结束后，关闭数据库链接
    def tearDownClass(cls):
        cls.data.close()
