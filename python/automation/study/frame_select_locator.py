from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from automation.dao.MysqlHelper import MySQLHelper

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

# 登录
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

# 进入内帧-->'menu-frame'
driver.switch_to.frame('menu-frame')

# 找到文字内容为‘商品列表’的‘a’链接，并点击进入
driver.find_element_by_link_text('商品列表').click()

# 退出内帧
driver.switch_to.default_content()

# 进入内帧-->'main-frame'
driver.switch_to.frame('main-frame')

# 找到添加商品的‘xpath’，并点击
driver.find_element_by_xpath('//a[@href="goods.php?act=add"]').click()

# 商品名
driver.find_element_by_name('goods_name').send_keys('铁蛋儿')

# 下拉框选择
Select(driver.find_element_by_name('cat_id')).select_by_visible_text('移动电源')

# 点击确定
driver.find_element_by_xpath('//input[@value=" 确定 "]').click()

# 等1秒钟
sleep(1)

# 进入商品列表页
driver.switch_to.default_content()
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()

driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

# 查找商品
Select(driver.find_element_by_name('cat_id')).select_by_visible_text('移动电源')
driver.find_element_by_name('keyword').send_keys('铁蛋儿')
driver.find_element_by_xpath('//input[@value=" 搜索 "]').click()

# 等1秒
sleep(1)

# 检查是否成功添加到数据库
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

# 关闭浏览器链接
driver.close()
# 关闭数据库链接
data.close()
