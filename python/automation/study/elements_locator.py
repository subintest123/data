from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('../drivers/chromedriver.exe')
# driver.get('http://192.168.1.36/ecshop/index.php')
# driver.maximize_window()
# driver.find_element_by_link_text('免费注册').click()
# sleep(1)
# driver.find_element_by_class_name('logo').click()
# sleep(1)
# driver.find_element_by_partial_link_text('注册').click()
# driver.find_element_by_name('username').send_keys('test123')
# driver.find_element_by_name('email').send_keys('312953732@qq.com')
# driver.find_element_by_name('password').send_keys('111111')
# driver.find_element_by_name('sel_question').click()
# driver.find_element_by_xpath("//input[@name='Submit']").click()


driver.get('http://192.168.48.136:8084/recruit.students/login/view')
driver.maximize_window()
driver.find_element_by_link_text('免费注册').click()
sleep(1)
driver.find_element_by_class_name('logo').click()
sleep(1)
driver.find_element_by_partial_link_text('注册').click()
driver.find_element_by_name('username').send_keys('test123')
driver.find_element_by_name('email').send_keys('312953732@qq.com')


