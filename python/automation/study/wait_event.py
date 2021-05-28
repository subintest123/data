from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC    # 引包--->expected_conditions，别名叫EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

WebDriverWait(driver, 4, 1).until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

sleep(1)
driver.switch_to.frame('header-frame')

WebDriverWait(driver, 2, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, '个人设置')), '对不起,找不到元素')
ActionChains(driver).move_to_element(driver.find_element_by_link_text('个人设置')).perform()
sleep(1)
WebDriverWait(driver, 3, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, '退出')), 'sorry').click()

sleep(2)
driver.close()