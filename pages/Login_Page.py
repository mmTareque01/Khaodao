import time
from appium.webdriver.common.appiumby import AppiumBy
from locators.Locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def lunch_login_page(self):
        return self.driver.find_element(AppiumBy.ID,
                                        Locators.skip_button_id).is_displayed() and self.driver.find_element(
            AppiumBy.ID, Locators.apply_button_id).is_displayed() and self.driver.find_element(AppiumBy.ID,
                                                                                               Locators.country_selector_id).is_displayed()

    def skip_login(self):
        self.driver.find_element(AppiumBy.ID, Locators.skip_button_id).click()

    def click_on_select_country(self):
        self.driver.find_element(AppiumBy.ID, Locators.country_selector_id).click()

    def select_all_country(self):
        self.click_on_select_country()
        time.sleep(3)
        return self.driver.find_elements(AppiumBy.ID, Locators.country_elements_id)

    def select_country(self):
        self.click_on_select_country()
        countries = self.driver.find_elements(AppiumBy.ID, Locators.country_elements_id)
        countries[1].click()

    def search_country_result(self, keyword):

        self.driver.find_element(AppiumBy.ID, Locators.search_country).click()
        self.driver.find_element(AppiumBy.ID, Locators.search_country).send_keys(keyword)
        return self.driver.find_elements(AppiumBy.ID, Locators.country_elements_id)

    def insert_phone_number(self, number=None):
        self.driver.find_element(AppiumBy.ID, Locators.number_input).send_keys(number)

    def apply_login(self):
        self.driver.find_element(AppiumBy.ID, Locators.apply_button_id).click()

    def login(self, number):
        self.select_country()
        self.insert_phone_number(number)
        self.apply_login()
        try:
            return self.driver.find_element(AppiumBy.ID, Locators.header_title).text == Locators.opt_msg and self.driver.find_element(AppiumBy.ID, Locators.resend_otp).is_displayed() and self.driver.find_element(AppiumBy.ID, Locators.verify_btn).is_displayed()
        except:
            return False