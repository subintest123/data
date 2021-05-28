# # 百度搜索
# from selenium import webdriver
#
# driver = webdriver.Chrome('../drivers/chromedriver.exe')
# driver.get('http://www.baidu.com')
# driver.maximize_window()
# driver.find_element_by_id('kw').send_keys('张国荣')
# driver.find_element_by_id('su').click()
# driver.close()

# # (1)
# # 登录‘ecshop’
# from selenium import webdriver
#
# # 导入Charmdriver驱动
# driver = webdriver.Chrome('../drivers/chromedriver.exe')
#
# # 进行自动化的网页URL--->get()
# driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
#
# # 窗口最大化
# driver.maximize_window()
#
# # 需要自动输入的文本--->send_keys()
# driver.find_element_by_name('username').send_keys('caichang')
# driver.find_element_by_name('password').send_keys('caichang1')
#
# # 点击--->click()
# driver.find_element_by_class_name('btn-a').click()
#
# # 关闭自动化--->close()
# driver.close()

# # (2)
# from selenium import webdriver
# from automation.dao.MysqlHelper import MySQLHelper
#
# data = MySQLHelper()
# data.host = '192.168.1.36'
# data.password = 'root'
# data.database = 'ecshop'
# query = 'select user_name,pwd from ecs_admin_user where user_id in (1,4,5)'
# result = data.select(query)
# print(result)
#
# for i in range(len(result)):
#     driver = webdriver.Chrome('../drivers/chromedriver.exe')
#     driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
#     driver.maximize_window()
#     driver.find_element_by_name('username').send_keys(f'{result[i][0]}')
#     driver.find_element_by_name('password').send_keys(f'{result[i][1]}')
#     driver.find_element_by_class_name('btn-a').click()
#     driver.close()
#
# data.close()

# (3)
from selenium import webdriver

from automation.dao.ExcelHelpr import ExcelHelper

data = ExcelHelper()
data.book_path = r'D:\mendao.xls'
data.sheet_name = 'Sheet2'
result = data.all_row_values(6, 8, 4, 6)

for i in range(len(result)):
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
    driver.maximize_window()
    driver.find_element_by_name('username').send_keys(f'{result[i][0]}')
    driver.find_element_by_name('password').send_keys(f'{result[i][1]}')
    driver.find_element_by_class_name('btn-a').click()
    driver.close()
