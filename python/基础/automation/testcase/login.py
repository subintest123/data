from selenium import webdriver


driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.97/zentao/user-login-L3plbnRhby8=.html')
driver.maximize_window()
driver.find_element_by_id('account').send_keys('admin')
driver.find_element_by_name('password').send_keys('root123456')
driver.find_element_by_id('submit').click()
