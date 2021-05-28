from selenium import webdriver

#打开浏览器
driver = webdriver.Chrome()

#打开指定的url地址的网页
driver.get('http://www.baidu.com')
#最大化浏览器
driver.maximize_window()
#找到元素
keyword = driver.find_element_by_id('kw')
#对这个元素输入内容
keyword.send_keys('caichang')

#找到元素
button = driver.find_element_by_id('su')
#对这个元素点击一下
button.click()
