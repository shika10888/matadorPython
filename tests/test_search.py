import re

from tests.test_base import TestBase


class TestSearch(TestBase):
    def test_atleast_one_image_url_should_contain_domain(self):
        domain = 'wallpapercave.com'
        has_domain = False
        for image in self.image_urls:
            if domain in image:
                has_domain = True
                break

        assert has_domain

    def test_atleast_one_title_should_have_car_or_cars(self):
        regex = ".*?\\b(?:car|cars)\\b.*?"
        has_match = False
        for title in self.title_urls:
            if re.search(regex, title.text.lower()):
                has_match = True
                break
        assert has_match
