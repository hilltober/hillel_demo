import pytest
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from lecture_windows_frames_alerts_selene.helpers.waiters import wait_for_alert


@pytest.mark.usefixtures('demoqa')
class TestAlerts:

    def test_browser_alerts(self):
        browser.open('alerts')
        activate_alert_button = s('#alertButton')
        activate_alert_button.click()
        alert = browser.switch_to.alert
        alert_txt = alert.text
        alert.accept()
        assert alert_txt == 'You clicked a button'

    def test_wait_for_alert(self):
        browser.open('alerts')
        s('#timerAlertButton').click()
        alert = wait_for_alert(browser, 6)
        alert_txt = alert.text
        alert.accept()
        assert alert_txt == 'This alert appeared after 5 seconds'

    def test_confirm_button_accept(self):
        browser.open('alerts')
        s('#confirmButton').click()
        alert = browser.switch_to.alert
        alert.accept()
        s('#confirmResult').should(have.text('Ok'))

    def test_confirm_button_decline(self):
        browser.open('alerts')
        s('#confirmButton').click()
        alert = browser.switch_to.alert
        alert.dismiss()
        s('#confirmResult').should(have.exact_text('You selected Cancel'))

    def test_prompt_box(self):
        browser.open('alerts')
        s('#promtButton').click()
        alert = browser.switch_to.alert
        alert.send_keys('ptn pnh')
        alert.accept()
        s('#promptResult').should(have.text('ptn pnh'))
