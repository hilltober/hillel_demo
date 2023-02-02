from selenium.webdriver import Chrome


def test_windows():
    driver = Chrome()
    driver.get('https://demoqa.com/browser-windows')
    
