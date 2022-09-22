import time

from appium.webdriver.common.appiumby import AppiumBy
from locators.Locators import Locators
from pages.Controller import Controller
from pages.Login_Page import LoginPage


class HomePage(Controller):
    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver

    def skip_login(self):
        LoginPage(self.driver).skip_login()

    def lunch_home_page(self):
        return self.driver.find_element(AppiumBy.ID, Locators.home_page_id).is_displayed()

    def allow_location(self):
        self.driver.find_element(AppiumBy.ID, Locators.allow_one_time).click()

    def take_out(self):
        return_data = False
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.take_out).click()
            return_data = self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()
        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.take_out).click()
            return_data = self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()
        else:
            print(1)

        return return_data

    def delivery(self):
        time.sleep(4)
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.delivery).click()
            return_data = self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()
        elif self.is_login_page():
            time.sleep(3)
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.delivery).click()
            return_data = self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.delivery).click()
            return self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()

        return return_data

    def qrc(self):
        time.sleep(4)
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.qrc).click()
            self.driver.find_element(AppiumBy.ID, Locators.allow_one_time).click()
            return_data = self.driver.find_element(AppiumBy.ID, Locators.scanner_id).is_displayed()
        elif self.is_login_page():
            time.sleep(3)
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.qrc).click()
            self.driver.find_element(AppiumBy.ID, Locators.allow_one_time).click()
            return_data = self.driver.find_element(AppiumBy.ID, Locators.scanner_id).is_displayed()
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.qrc).click()
            self.driver.find_element(AppiumBy.ID, Locators.allow_one_time).click()
            return self.driver.find_element(AppiumBy.ID, Locators.scanner_id).is_displayed()

        return return_data

    def cancel(self):
        self.driver.find_element(AppiumBy.ID, Locators.cancel_btn_id).click()

    def navigate_to_order(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.order_page).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.order_page).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.order_page).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

    def navigate_to_favourite(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.favourite_page).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.favourite_page).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.favourite_page).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

    def navigate_to_profile(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.profile).click()
            return self.driver.find_element(AppiumBy.ID, Locators.profile_page).is_displayed()

        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.profile).click()
            return self.driver.find_element(AppiumBy.ID, Locators.profile_page).is_displayed()
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.profile).click()
            return self.driver.find_element(AppiumBy.ID, Locators.profile_page).is_displayed()

    def profile_view(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.profile_view).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.profile_view).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.profile_view).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

    def add_new_address(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.address).click()
            self.driver.find_element(AppiumBy.ID, Locators.add_new_address).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.address).click()
            self.driver.find_element(AppiumBy.ID, Locators.add_new_address).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.address).click()
            self.driver.find_element(AppiumBy.ID, Locators.add_new_address).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.title).text == Locators.login_required
            return is_matched

    def navigate_to_plate(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.plate_btn).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.alert_dialogue_title).text == Locators.my_plate
            self.driver.find_element(AppiumBy.ID, Locators.ok_dialogue_btn)
            return is_matched

        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.plate_btn).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.alert_dialogue_title).text == Locators.my_plate
            self.driver.find_element(AppiumBy.ID, Locators.ok_dialogue_btn)
            return is_matched
        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.plate_btn).click()
            is_matched = self.driver.find_element(AppiumBy.ID, Locators.alert_dialogue_title).text == Locators.my_plate
            self.driver.find_element(AppiumBy.ID, Locators.ok_dialogue_btn)
            return is_matched

    def filter(self):
        if self.is_home_page():
            self.driver.find_element(AppiumBy.ID, Locators.filter_button).click()
            self.driver.find_element(AppiumBy.ID, Locators.two_digit_price).click()
            self.driver.find_element(AppiumBy.ID, Locators.find_btn).click()
            return self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()


        elif self.is_login_page():
            self.skip_login()
            self.allow_location()
            self.driver.find_element(AppiumBy.ID, Locators.filter_button).click()
            self.driver.find_element(AppiumBy.ID, Locators.two_digit_price).click()
            self.driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/findButton').click()
            return self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()


        else:
            self.driver.back()
            self.driver.find_element(AppiumBy.ID, Locators.filter_button).click()
            self.driver.find_element(AppiumBy.ID, Locators.two_digit_price).click()
            self.driver.find_element(AppiumBy.ID, Locators.find_btn).click()
            return self.driver.find_element(AppiumBy.ID, Locators.restaurent_list).is_displayed()

    def add_to_plate(self):
        print()

    def price_calculation(self):
        print()

    # def navigate_to_favorites(self):

    # def navigate_to_more(self):
