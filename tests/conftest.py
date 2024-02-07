import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from configuration.config import TestData
from pom.searchPage import SearchPage
from pom.searchResultsPage import SearchResultsPage


@pytest.fixture(scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    web_driver.maximize_window()
    web_driver.get(TestData.Base_Url)
    request.cls.driver = web_driver
    search_page = SearchPage(web_driver)
    search_page.search("nice cars images")
    search_result = SearchResultsPage(web_driver)
    images = search_result.get_images()
    image_urls = []
    for image in images:
        image_urls.append(image.get_attribute('href').split('&iai=')[1])
    request.cls.image_urls = image_urls
    request.cls.title_urls = search_result.get_titles()

    yield
    web_driver.close()
