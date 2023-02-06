from selene.core import query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class TestWindows:

    def test_browser_windows_1(self):
        browser.open('browser-windows')
        new_tab_button = s('#tabButton')
        new_tab_button.click()
        new_tab = browser.switch_to_tab(1)
        msg = s('#sampleHeading').get(query.text)
        new_tab.close()
        browser.switch_to_tab(0)
        assert msg == 'This is a sample page'

    def test_browser_windows_2(self):
        browser.open('browser-windows')
        new_window_button = s('#windowButton')
        new_window_button.click()
        new_window = browser.switch_to_tab(1)
        txt = new_window.element('#sampleHeading').get(query.text)
        new_window.close()
        browser.switch_to_tab(0)
        assert txt == 'This is a sample page'

    def test_browser_windows_3(self):
        browser.open('browser-windows')
        new_message_button = s('#messageWindowButton')
        new_message_button.click()
        new_msg_window = browser.switch_to_tab(1)
        res = browser.element('//body').get(query.text)
        new_msg_window.close()
        assert 'your friends' in res
