import time

from selenium.webdriver.common.by import By

from pom.configurationPage import ConfigurationPage


class SearchPage(ConfigurationPage):
    search_edit_box = (By.ID, 'searchbox_input')
    search_button = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, search_text):
        self.search_keyword(self.search_edit_box, search_text)
        time.sleep(1)
        self.click(self.search_button)
        time.sleep(5)
