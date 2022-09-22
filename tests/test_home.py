import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from pages.Home_Page import HomePage
from tests.test_base import TestBase
from pages.Login_Page import LoginPage

# pytest tests/test_home.py::TestHomePage::lunch_home_page
# pytest tests/test_login.py::TestLoginPage::test_select_country_search_with_invalid_keyword


class TestHomePage(TestBase):

    def test_lunch_home_page(self):
        home_obj = HomePage(self.driver)
        home_obj.skip_login()
        assert home_obj.lunch_home_page()

    def test_allow_location(self):
        home_obj = HomePage(self.driver)
        LoginPage(self.driver).skip_login()
        home_obj.allow_location()
        assert home_obj.is_home_page()

    def test_take_out(self):
        home_obj = HomePage(self.driver)
        assert home_obj.take_out()

    def test_delivery(self):
        home_obj = HomePage(self.driver)
        assert home_obj.delivery()

    def test_qrc(self):
        home_obj = HomePage(self.driver)
        assert home_obj.qrc()

    def test_navigate_to_order(self):
        home_obj = HomePage(self.driver)
        status = home_obj.navigate_to_order()
        home_obj.cancel()
        assert status

    def test_navigate_to_favourite(self):
        home_obj = HomePage(self.driver)
        status = home_obj.navigate_to_favourite()
        home_obj.cancel()
        assert status

    def test_navigate_to_profile(self):
        home_obj = HomePage(self.driver)
        status = home_obj.navigate_to_profile()
        assert status

    def test_profile_view(self):
        home_obj = HomePage(self.driver)
        status = home_obj.profile_view()
        home_obj.cancel()
        assert status

    def test_add_new_address(self):
        home_obj = HomePage(self.driver)
        status = home_obj.add_new_address()
        home_obj.cancel()
        assert status

    def test_my_plate(self):
        home_obj = HomePage(self.driver)
        status = home_obj.navigate_to_plate()
        assert status

    def test_filter(self):
        home_obj = HomePage(self.driver)
        status = home_obj.filter()
        assert status




