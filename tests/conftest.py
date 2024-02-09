import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from configuration.config import TestData
from pom.searchPage import SearchPage
from pom.searchResultsPage import SearchResultsPage


@pytest.fixture
def init_driver(request):
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    web_driver.maximize_window()
    web_driver.get(TestData.Base_Url)
    request.cls.driver = web_driver
    search_page = SearchPage(web_driver)
    search_page.search("nice cartoons images")
    failed_before = request.session.testsfailed
    yield
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        print(test_name)
        web_driver.save_screenshot("C:/Users/alvin/PycharmProjects/matadorPython/screenshots/" + test_name + ".png")
    web_driver.close()
