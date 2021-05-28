from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_class_name('btn-a').click()
print(driver.switch_to.alert.text)
#print(driver.switch_to_alert().text) 可以但被弃用

if driver.switch_to.alert.text==r'- 管理员用户名不能为空!':
    #print(driver.switch_to.alert.text) #获取弹框中的文字内容
    driver.switch_to.alert.accept()#点击确定 如果是点取消用dismiss
    driver.find_element_by_name('username').send_keys('caichang')
