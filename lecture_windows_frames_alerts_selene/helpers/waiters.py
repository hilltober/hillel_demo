import time
from selene.support.shared import SharedBrowser
from selenium.common import NoAlertPresentException


def wait_for_alert(driver: SharedBrowser, timeout=10):
    alert = None
    end_time = time.monotonic() + timeout
    while time.monotonic() <= end_time:
        try:
            alert = driver.switch_to.alert
            break
        except NoAlertPresentException:
            time.sleep(0.1)
            continue
    if alert:
        return alert
    else:
        raise NoAlertPresentException(f'No alert during {timeout} seconds')
