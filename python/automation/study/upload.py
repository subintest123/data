# 上传文件--->input标签
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 引包--->expected_conditions，别名叫EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()

driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

driver.find_element_by_xpath('//a[@href="goods.php?act=add"]').click()

# 定位到上传属性，后面跟文件路径
WebDriverWait(driver, 2, 1).until(EC.visibility_of_element_located((By.NAME, 'goods_img')), 'sorry not fount').send_keys(r'D:\subin\logo.jpg')
