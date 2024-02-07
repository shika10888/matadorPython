from selenium.webdriver.common.by import By
from pom.configurationPage import ConfigurationPage


class SearchResultsPage(ConfigurationPage):
    search_images = (By.XPATH, '//div[@class="module--images__thumbnails js-images-thumbnails"]/div/a')
    search_titles = (By.XPATH, '//a[@data-testid="result-title-a"]/span')

    def __init__(self, driver):
        super().__init__(driver)

    def get_titles(self):
        return self.driver.find_elements(*self.search_titles)

    def get_images(self):
        return self.driver.find_elements(*self.search_images)

