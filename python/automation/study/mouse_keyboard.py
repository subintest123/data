from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')

# 通过键盘粘贴（需要先复制到剪切板）
driver.find_element_by_name('username').send_keys(Keys.CONTROL, 'v')
driver.find_element_by_name('password').send_keys('caichang1')
sleep(1)

# 定位到元素后 ，键盘回车
driver.find_element_by_class_name('btn-a').send_keys(Keys.ENTER)

# 窗口最小化
driver.minimize_window()
sleep(2)

# 窗口最大化
driver.maximize_window()
sleep(2)

driver.switch_to.frame('header-frame')
sleep(1)

# 鼠标移动到某个位置
ActionChains(driver).move_to_element(driver.find_element_by_link_text('个人设置')).perform()

# 点击某个元素
driver.find_element_by_link_text('退出').click()
sleep(2)

# 前进页面
driver.forward()
sleep(2)

# 回退页面
driver.back()
sleep(2)

# 刷新页面
driver.refresh()
sleep(2)

# 关闭自动化窗口
driver.close()



