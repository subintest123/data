from time import sleep
from selenium import webdriver
from automation.dao.MySQLHelper import MySQLHelper

'''
result = driver.find_element_by_xpath('//div[@id="turn-page"]/span').text
获得页面文本的写法:参数=先找到元素().text
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

driver.find_element_by_name('keyword').send_keys('海王')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()

sleep(1)

table_text=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
result = driver.find_element_by_xpath('//div[@id="turn-page"]/span').text

sleep(1)

data = MySQLHelper()
data.host = '192.168.1.36'
data.password = 'root'
data.database = 'ecshop'
query = "select goods_name from ecs_goods where goods_name='尧海王'"
total = "select count(*) from ecs_goods where goods_name='尧海王'"
result = data.select(query,'one')
total_result = data.select(total,'one')


if result[0]=='尧海王' and total_result[0]==1:
    print('测试通过')
else:
    print('测试不通过')


driver.close()
data.close()
