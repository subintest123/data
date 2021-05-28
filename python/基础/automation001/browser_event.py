from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.minimize_window()
sleep(4)
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()

