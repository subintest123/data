from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from automation.utils.Config import Config
from automation.utils.Logger import Logger

logger = Logger('BasePage').getlog()


class BasePage():

    file = './conf/config.ini'    # 指定配置文件的路径
    config = Config(file)    # 导入配置文件

    def __init__(self):
        self.driver = None

    # 打开配置文件中定义的链接
    def open(self):
        self.driver = webdriver.Chrome(self.config.get_value(self.file, 'base', 'chrome_driver'))
        self.driver.get(self.config.get_value(self.file, 'base', 'url'))

    # ‘waitElemnet’用来指定查找元素时的等待时间，找到/超时就结束查找
    def __waitElemnet(self, selector_by, selector_value, secs=5):
        try:
            if selector_by == "id":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.ID, selector_value)))
            elif selector_by == "name":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.NAME, selector_value)))
            elif selector_by == "link_text":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.LINK_TEXT, selector_value)))
            elif selector_by == "partial_link_text":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
            elif selector_by == "xpath":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.XPATH, selector_value)))
            elif selector_by == "class_name":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME, selector_value)))
            elif selector_by == "css_selector":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector_value)))
            else:
                raise NoSuchElementException("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")

        except (TimeoutException, NoSuchElementException):
            print('超时或找不到元素')

    def find_element(self, selector):
        # 根据=>来切割字符串，如：submit_btn = "id=>caichang"

        if '=>' not in selector:
            raise Exception('对不起，至少要包含=>符')

        # 如果包含了=>字符传后开始切割
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # 查找元素，超时抛异常
        self.__waitElemnet(selector_by, selector_value)

        if selector_by == 'id':    # 通过‘ID’元素定位
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == 'name':    # 通过‘name’元素定位
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'link_text':    # 通过‘link_text’元素定位‘a’链接（全匹配）
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'partial_link_text':    # 定位‘a’链接，部分匹配，
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'xpath':    # 通过复制的元素‘xpath’定位
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == 'class_name':    # 通过‘class_name’元素定位
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            element = self.driver.find_element_by_css_selector(selector_value)
        return element

    # 页面中的输入文本的元素
    def input(self, selector, value):
        self.find_element(selector).send_keys(value)

    # 定位器(selector)点击页面中的...元素
    def click(self, selector):
        self.find_element(selector).click()

    # 进入内帧
    def into_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 退出内帧
    def out_frame(self):
        self.driver.switch_to.default_content()

    # 通过链接后的文字内容，查找页面中的‘a’链接
    def select_by_text(self, selector, text):  # 定位器--->链接文本
        Select(self.find_element(selector)).select_by_visible_text(text)

    # 关闭浏览器
    def close_bowser(self):
        self.driver.close()

    # 通过选择器获得属性的最后一个值
    def get_goods_isonsale(self, selector, attribute):
        src_property = self.find_element(selector).get_attribute(attribute).split('/')[-1]
        return src_property
