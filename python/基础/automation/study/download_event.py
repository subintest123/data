from selenium import webdriver

options = webdriver.ChromeOptions()
prefs={
    "download.prompt_for_download": False,
    'download.default_directory': 'd:/',#下载目录
    "plugins.always_open_pdf_externally": True,
    'profile.default_content_settings.popups': 0,#设置为0，禁止弹出窗口
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=options)
driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

# 进入内帧
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('模板选择').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')

driver.find_element_by_id('backup').click()