from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
#driver.find_element_by_name('username').send_keys('caichang')

driver.find_element_by_name('username').send_keys(Keys.CONTROL,'v') #键盘组合键的写法
driver.find_element_by_name('password').send_keys('caichang1')


#键盘点击回车
#键盘采用Keys这个类,他里面只有一些静态属性
driver.find_element_by_class_name('btn-a').send_keys(Keys.ENTER)

driver.switch_to.frame('header-frame')
#driver.find_element_by_link_text('个人设置').click()


#鼠标用ActionChains这个类,请自行定位类去看方法并学习
ActionChains(driver).move_to_element(driver.find_element_by_link_text('个人设置')).perform()
driver.find_element_by_link_text('退出').click()


