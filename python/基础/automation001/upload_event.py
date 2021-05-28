from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

from automation.dao.MySQLHelper import MySQLHelper

driver = webdriver.Chrome()
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

# 进入内帧
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()

# 退出内帧
driver.switch_to.default_content()
# 进入新的内帧
driver.switch_to.frame('main-frame')
driver.find_element_by_xpath('//a[@href="goods.php?act=add"]').click()

driver.find_element_by_name('goods_name').send_keys('凤姐球鞋')

Select(driver.find_element_by_name('cat_id')).select_by_visible_text('移动电源')

driver.find_element_by_name('goods_img').send_keys(r'E:\crm\Public\Images\logo.png')
