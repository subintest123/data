from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC    # 引包-->expected_conditions，取个别名叫-->EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    'download.default_directory': 'd:/',    # 下载目录
    "plugins.always_open_pdf_externally": True,
    'profile.default_content_settings.popups': 0,   # 设置为0，禁止弹出窗口
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome('../drivers/chromedriver.exe', options=options)
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
WebDriverWait(driver, 2, 1).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys('caichang1')
WebDriverWait(driver, 3, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-a'))).click()

# 进入内帧
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('模板选择').click()
# 退出内帧
driver.switch_to.default_content()
# 进入另一个内帧
driver.switch_to.frame('main-frame')

# 找到‘backup’，点击进行下载
driver.find_element_by_id('backup').click()
