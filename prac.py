import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

#this page is just for testing any functionality

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Android Emulator",
  "appium:app": "/home/mm/mobile-apps/KhaoDao.apk"
}
path = '0.0.0.0:4723/wd/hub'

driver = webdriver.Remote(path, desired_cap)

time.sleep(3)

# aaa = driver.find_element(AppiumBy.ID, "com.graaho.khaodao:id/skipImageView").is_displayed()
#
# print(">>>>>>>>> ", aaa)

driver.find_element(AppiumBy.ID, "com.graaho.khaodao:id/skipImageView").click()
# driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/rlClickConsumer').click()
time.sleep(2)

driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button').click()
time.sleep(2)

driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/navigation_my_orders').click()
time.sleep(3)
a = driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/titleTv').text
print(">>>>>>>>>>>>   ", a)
# driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/editText_search').click()
# time.sleep(2)
# driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/editText_search').send_keys("ca")
# driver.back()
# driver.
# driver.press_keycode(31, 29)
# time.sleep(1)
# # driver.press_keycode(29)
# time.sleep(1)
# driver.press_keycode(66)


# countries = driver.find_elements(AppiumBy.ID, "com.graaho.khaodao:id/textView_countryName")
# countries[2].click()
# time.sleep(2)
# driver.find_element(AppiumBy.ID, 'com.graaho.khaodao:id/mobileNumberET').send_keys("434444")
# driver.close()
