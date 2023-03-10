import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By

test_setup = {
    'calculator': {
        'platformName': 'Android',
        'platformVersion': '12.0',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.google.android.calculator',
        'appActivity': 'com.android.calculator2.Calculator'}
}


@pytest.fixture(scope='function')
def calc():
    driver = webdriver.Remote(
        'http://localhost:4723/wd/hub',
        test_setup.get('calculator'))
    yield driver
    driver.find_element(By.ACCESSIBILITY_ID, 'clear').click()
    driver.quit()


class TestCalculator:

    def test_calc_addition(self, calc):
        one = calc.find_element(By.ACCESSIBILITY_ID, '1')
        two = calc.find_element(By.ACCESSIBILITY_ID, '2')
        plus = calc.find_element(By.ACCESSIBILITY_ID, 'plus')
        equals = calc.find_element(By.ACCESSIBILITY_ID, 'equals')

        one.click()
        plus.click()
        two.click()
        equals.click()
        result = calc.find_element(
            By.ID, 'com.google.android.calculator:id/result_final')

        assert result.text == '3'

