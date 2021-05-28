from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
sleep(2)

driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('header-frame')

WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.LINK_TEXT,'个人设置')),'对不起,找不到元素')
ActionChains(driver).move_to_element(driver.find_element_by_link_text('个人设置')).perform()


WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.LINK_TEXT,'退出')),'对不起,找不到元素')
driver.find_element_by_link_text('退出').click()







