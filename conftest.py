import pytest
from selene.support.shared import config, browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='package', name='demoqa', autouse=True)
def set_browser_for_demoqa():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=chrome_options)
    config.base_url = 'https://demoqa.com/'
    config.driver = driver
    yield driver
    browser.quit()
