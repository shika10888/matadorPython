import re

from pom.searchResultsPage import SearchResultsPage
from tests.test_base import TestBase


class TestSearch(TestBase):
    def test_atleast_one_image_url_should_contain_domain(self):
        search_result = SearchResultsPage(self. driver)
        images = search_result.get_images()
        image_urls = []
        for image in images:
            image_urls.append(image.get_attribute('href').split('&iai=')[1])
        domain = 'wallpapercaveshika.com'
        has_domain = False
        for image in image_urls:
            if domain in image:
                has_domain = True
                break

        assert has_domain

    def test_atleast_one_title_should_have_car_or_cars(self):
        search_result = SearchResultsPage(self.driver)
        title_urls = search_result.get_titles()
        regex = ".*?\\b(?:car|cars)\\b.*?"
        has_match = False
        for title in title_urls:
            if re.search(regex, title.text.lower()):
                has_match = True
                break
        assert has_match
