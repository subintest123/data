from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

from automation.dao.MySQLHelper import MySQLHelper

'''
内帧:
    1.进入内帧:driver.switch_to.frame('menu-frame')
    2.退出内帧:driver.switch_to.default_content()
    
下拉框:
    Select(driver.find_element_by_name('cat_id')).select_by_visible_text('移动电源')
        注意:我们大多采用这个方法,因为用下拉框的名字要好很多:select_by_visible_text
            当然,也有其他的方法,自己跟代码看(index,value均可)
    
            
'''
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

driver.find_element_by_xpath('//input[@value=" 确定 "]').click()

sleep(1)

data = MySQLHelper()
data.host = '192.168.1.36'
data.password = 'root'
data.database = 'ecshop'
query = "select goods_name from ecs_goods where goods_name='凤姐球鞋'"
result = data.select(query,'one')
print(result)
if result[0]=='凤姐球鞋':
    print('测试通过')
else:
    print('测试不通过')
driver.close()
data.close()