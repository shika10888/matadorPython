import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    web_driver.maximize_window()
    web_driver.get("https://duckduckgo.com/")
    request.cls.driver = web_driver
    yield
    web_driver.close()
