from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').send_keys(Keys.ENTER)    # 通过键盘回车点击

driver.minimize_window()
sleep(2)
driver.maximize_window()

