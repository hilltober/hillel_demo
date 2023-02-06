import time
from selenium.common import WebDriverException, InvalidElementStateException, \
    NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def set_checkbox_state(driver: WebDriver,
                       folder_name: str,
                       enabled: bool = True) -> None:
    folder = driver.find_element(
        By.XPATH,
        f'//span[@class="rct-title"][.="{folder_name}"]'
        f'//ancestor::span[@class="rct-text"]')
    _ = folder.location_once_scrolled_into_view
    fold_input = folder.find_element(By.CSS_SELECTOR, 'input[id]')
    fold_checkbox = folder.find_element(By.CSS_SELECTOR, 'label[for]')
    if enabled:
        if not fold_input.is_selected():
            fold_checkbox.click()
    else:
        if fold_input.is_selected():
            fold_checkbox.click()


def select_folder(driver: WebDriver, folder_name: str, enabled=True):
    set_checkbox_state(driver, folder_name, enabled=enabled)


def select_folders(driver: WebDriver = None, folders: list = None):
    if folders:
        for folder in folders:
            select_folder(driver, folder, enabled=True)


def expand_full_tree(driver: WebDriver):
    expand_button = driver.find_element(
        By.CSS_SELECTOR, 'button[aria-label="Expand all"]')
    expand_button.click()


def optimize_test_data(data: list):
    return {'tree': [d.capitalize() for d in data],
            'results': [r.lower() for r in data]}


def expand_folder(driver: WebDriver, folder_name: str):
    expand_button = driver.find_element(
        By.XPATH, f'//span[@class="rct-text"][.="{folder_name}"]'
                  f'/button[@aria-label="Toggle"]')
    _ = expand_button.location_once_scrolled_into_view
    expand_button.click()


def expand_folders(driver: WebDriver, folders: list):
    for folder in folders:
        expand_folder(driver, folder)


def is_element_enabled(driver, locator, timeout):
    is_enabled = False
    end_time = time.monotonic() + timeout
    is_element_in_dom(driver, locator)
    while time.monotonic() <= end_time:
        if driver.find_element(*locator).is_enabled():
            is_enabled = True
            break
        else:
            continue
    if is_enabled:
        return True
    else:
        raise InvalidElementStateException(
            f'element is present in DOM,'
            f' but not enabled after {timeout + 1} sec.')


def is_element_in_dom(driver, locator):
    try:
        _ = driver.find_element(*locator)
        return True
    except WebDriverException:
        raise
