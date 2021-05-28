from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.97/zentao/user-login-L3plbnRhby8=.html')
driver.maximize_window()
driver.find_element_by_id('account').send_keys('admin')
driver.find_element_by_name('password').send_keys('root123456')
driver.find_element_by_id('submit').click()

WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH,'//li[@title="项目集"]')),'对不起,找不到元素')

driver.find_element_by_xpath('//li[@title="项目集"]').click()
driver.find_element_by_id('app-program').click()

driver.switch_to.frame('appIframe-program')
driver.find_element_by_css_selector('.btn-secondary').click()

driver.find_element_by_id('name').send_keys('自动化测试项目集5')

driver.find_element_by_xpath('//*[@id="PM_chosen"]/a/span').click()
driver.find_element_by_xpath('//*[@id="PM_chosen"]/a').send_keys('C:蔡昶',Keys.ENTER)

driver.find_element_by_id('end').send_keys('2021-05-20',Keys.ENTER)

number = randint(0,4)
driver.find_elements_by_name('delta')[number].click()

#print(driver.find_elements_by_tag_name("iframe"))
driver.switch_to.frame(0)
driver.find_element_by_class_name('article-content').send_keys('cccc')

driver.switch_to.default_content()
driver.switch_to.frame('appIframe-program')

#文本区自己研究一下
driver.find_element_by_xpath('//*[@id="submit"]').click()


#driver.switch_to.frame('appIframe-program')
#print(driver.find_element_by_xpath('//*[@id="programTableList"]/tr[2]/td[1]/a').text)
