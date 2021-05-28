# 无头模式
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 引包--->expected_conditions，别名叫EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# 无头模式,不启动浏览器,在底层运行
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome('../drivers/chromedriver.exe', options=options)
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')

WebDriverWait(driver, 2, 1).until(EC.visibility_of_element_located((By.NAME, 'username')), 'sorry,not fount').send_keys('caichang')
WebDriverWait(driver, 2, 1).until(EC.visibility_of_element_located((By.NAME, 'password')), 'sorry,not fount').send_keys('caichang1')
WebDriverWait(driver, 2, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-a')), 'sorry,not fount').click()
driver.close()
print(123)
