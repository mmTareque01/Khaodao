from appium import webdriver


def configuration():
    desired_cap = {
        "platformName": "Android",
        "appium:deviceName": "Android Emulator",
        "appium:app": "/home/mm/mobile-apps/KhaoDao.apk"
    }
    path = '0.0.0.0:4723/wd/hub'
    return webdriver.Remote(path, desired_cap)
