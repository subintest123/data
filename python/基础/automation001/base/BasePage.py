from selenium import webdriver


class BasePage():

    def drivers(self):
        driver = webdriver.Chrome('../automation/drivers/chromedriver.exe')
        return driver

    def open(self, url):
        self.drivers().get(url)

    def max_browser(self):
        self.drivers().maximize_window()

    def input_by_id(self, id, value):
        self.drivers().find_element_by_id(id).send_keys(value)

    def input_by_name(self, name, value):
        self.drivers().find_element_by_name(name).send_keys(value)
