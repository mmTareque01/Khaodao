from appium.webdriver.common.appiumby import AppiumBy

from locators.Locators import Locators


class Controller:
    def __init__(self, driver):
        self.driver = driver

    def is_login_page(self):
        try:
            return self.driver.find_element(AppiumBy.ID,
                                            Locators.skip_button_id).is_displayed() and self.driver.find_element(
                AppiumBy.ID, Locators.apply_button_id).is_displayed() and self.driver.find_element(AppiumBy.ID,
                                                                                                   Locators.country_selector_id).is_displayed()
        except:
            return False

    def is_home_page(self):
        try:
            return self.driver.find_element(AppiumBy.ID, Locators.home_page).is_displayed()

        except:
            return False

        return False

    def is_more_page(self):
        try:
            return self.driver.find_element(AppiumBy.ID, Locators.more_page).is_displayed()
        except:
            return False

    def is_order(self):
        return 1

    def is_favourite(self):
        return 1
