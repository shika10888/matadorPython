import pytest
from selenium.webdriver.common.by import By

from pom.searchPage import SearchPage
from pom.searchResultsPage import SearchResultsPage
from tests.test_base import TestBase


class TestSearch(TestBase):
    def test_get_titles(self):
        self.search1 = SearchPage(self.driver)
        self.search1.search("nice cars")
        self.search_results = SearchResultsPage(self.driver)
        for ele in self.search_results.get_titles(self.search_results.search_titles):
            print(ele.text)
