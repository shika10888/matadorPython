from selenium.webdriver.common.by import By

from pom.configurationPage import ConfigurationPage


class SearchResultsPage(ConfigurationPage):
    search_images = (By.CLASS_NAME, 'module--images')
    search_titles = (By.XPATH, '//a[@data-testid="result-title-a"]/span')

    def __init__(self, driver):
        super().__init__(driver)

    def get_titles(self, by_locator):
        return self.driver.find_elements(*by_locator)

