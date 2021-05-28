from selenium import webdriver

from automation.dao.ExcelHelper import ExcelHelper
from automation.dao.MySQLHelper import MySQLHelper


data =ExcelHelper()
data.book_path=r'd:\mendao.xls'
data.sheet_name='Sheet2'
result = data.allvalues_by_row(7,9,7,9)


for i in range(len(result)):

    driver = webdriver.Chrome()
    driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
    driver.maximize_window()

    driver.find_element_by_name('username').send_keys(f'{result[i][0]}')
    driver.find_element_by_name('password').send_keys(f'{result[i][1]}')
    driver.find_element_by_class_name('btn-a').click()


driver.close()





