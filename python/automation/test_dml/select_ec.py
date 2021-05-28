from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from automation.dao.MysqlHelper import MySQLHelper

driver = webdriver.Chrome()
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

Select(driver.find_element_by_name('cat_id')).select_by_visible_text('移动电源')
driver.find_element_by_name('keyword').send_keys('铁蛋儿')
driver.find_element_by_xpath('//input[@value=" 搜索 "]').click()
sleep(1)

data = MySQLHelper()
data.host = '192.168.1.36'
data.password = 'root'
data.database = 'ecshop'
query = "select * from ecs_goods where goods_name='铁蛋儿'"
result = data.select(query, 'one')
print(result)
if result[3] == '铁蛋儿':
    print('测试通过')
else:
    print('测试不通过')

driver.close()
data.close()
