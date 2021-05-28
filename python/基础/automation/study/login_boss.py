from selenium import webdriver

from automation.dao.MySQLHelper import MySQLHelper

data = MySQLHelper()
data.host = '192.168.1.36'
data.password = 'root'
data.database = 'ecshop'
query = 'select user_name,pwd from ecs_admin_user where user_id in (1,4,5)'
result = data.select(query)
print(result)

for i in range(len(result)):

    driver = webdriver.Chrome()
    driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
    driver.maximize_window()

    driver.find_element_by_name('username').send_keys(f'{result[i][0]}')
    driver.find_element_by_name('password').send_keys(f'{result[i][1]}')
    driver.find_element_by_class_name('btn-a').click()

data.close()

driver.close()





