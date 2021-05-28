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
    file = './conf/config.ini'
    config = Config(file)

    def __init__(self):
        self.driver = None

    def open(self):

        self.driver = webdriver.Chrome(self.config.get_value(self.file, 'base', 'chrome_driver'))
        self.driver.get(self.config.get_value(self.file, 'base', 'url'))
        # logger.info(f"打开的浏览器地址为:{self.driver.get(self.file, 'base', 'url')}")
        self.driver.maximize_window()
        logger.info('你最大化了浏览器')

    def __waitElemnet(self, selector_by, selector_value, secs=5):
        try:
            # 实在写不下去所有了，自己扩展出所有，一般感觉有这些够了
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
                logger.info("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")
                raise NoSuchElementException("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")

        except (TimeoutException, NoSuchElementException):
            logger.info('超时或找不到元素')
            print('超时或找不到元素')

    def find_element(self, selector):
        # 根据=>来切割字符串，submit_btn = "id=>caichang"

        element = ''

        if '=>' not in selector:
            logger.info('对不起，至少要包含=>符')
            raise Exception('对不起，至少要包含=>符')

        # 如果包含了=>字符传后开始切割
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # 查找元素，超时抛异常
        self.__waitElemnet(selector_by, selector_value)

        # 实在写不下去所有了，自己扩展出所有，一般感觉有这些够了
        if selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            element = self.driver.find_element_by_css_selector(selector_value)
        return element

    def input(self, selector, value):
        self.find_element(selector).send_keys(value)

    def click(self, selector):
        self.find_element(selector).click()

    def into_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    def out_frame(self):
        self.driver.switch_to.default_content()

    def select_by_text(self, selector, text):
        Select(self.find_element(selector)).select_by_visible_text(text)

    # 通过选择器获得属性的最后一个值
    def get_goods_isonsale_ico(self, selector, attribute):
        src_property = self.find_element(selector).get_attribute(attribute).split('/')[-1]
        return src_property

    def close_browser(self):
        self.driver.close()
