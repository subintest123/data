from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

from automation.dao.MysqlHelper import MySQLHelper

# 加载驱动
driver = webdriver.Chrome()
# 打开链接
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
# 最大化窗口
driver.maximize_window()

# 登录账户
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

# 进入内帧
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()

# 退出内帧
driver.switch_to.default_content()

# 进入另一个内帧
driver.switch_to.frame('main-frame')

# 查询商品
Select(driver.find_element_by_name('cat_id')).select_by_visible_text('移动电源')
driver.find_element_by_name('keyword').send_keys('小黑')
driver.find_element_by_xpath('//input[@value=" 搜索 "]').click()

sleep(1)

src_property = \
    driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').get_attribute('src').split('/')[
        -1]

sleep(1)

if src_property == 'no.gif':
    src_property = 0
else:
    src_property = 1

# 设置商品上/下架，并验证数据库
data = MySQLHelper()
data.host = '192.168.1.36'
data.password = 'root'
data.database = 'ecshop'
query = "select goods_name,is_on_sale from ecs_goods where goods_name like '%小黑%'"
result = data.select(query, 'one')

if result[1] == src_property:
    driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img').click()
    sleep(1)
    sql = "select goods_name,is_on_sale from ecs_goods where goods_name like '%小黑%'"
    result = data.select(sql, 'one')
    if result[1] == 1:
        print('测试通过')
    else:
        print('测试不通过')
else:
    print('页面有变更或sql有错误')
