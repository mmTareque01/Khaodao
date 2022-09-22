import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from pages.Home_Page import HomePage
from tests.test_base import TestBase
from pages.Login_Page import LoginPage


class TestLoginPage(TestBase):


    def test_lunch_login_page(self):
        login_page_obj = LoginPage(self.driver)
        time.sleep(5)
        assert login_page_obj.lunch_login_page()

    def test_skip(self):
        login_page_obj = LoginPage(self.driver)
        time.sleep(5)
        login_page_obj.skip_login()
        time.sleep(3)
        assert HomePage(self.driver).lunch_home_page()

    def test_select_country(self):
        login_page_obj = LoginPage(self.driver)
        time.sleep(3)
        total_countries = login_page_obj.select_all_country()
        assert len(total_countries) > 0

    def test_select_country_search_with_valid_keyword(self):
        login_page_obj = LoginPage(self.driver)
        time.sleep(3)
        total_countries_before_search = login_page_obj.select_all_country()
        time.sleep(2)
        country_list_after_search = login_page_obj.search_country_result('ca')
        assert len(total_countries_before_search) > len(country_list_after_search)


    def test_select_country_search_with_invalid_keyword(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.click_on_select_country()
        country_list_after_search = login_page_obj.search_country_result('#')
        assert len(country_list_after_search) == 0

    def test_apply_without_number(self):
        login_page_obj = LoginPage(self.driver)
        assert not login_page_obj.login("")

    def test_apply_using_invalid_number(self):
        login_page_obj = LoginPage(self.driver)
        assert not login_page_obj.login("dfkdpkf")

    def test_apply_using_valid_number(self):
        login_page_obj = LoginPage(self.driver)
        assert login_page_obj.login("01793899433")
