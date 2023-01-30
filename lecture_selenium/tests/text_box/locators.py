from selenium.webdriver.common.by import By

CSS = By.CSS_SELECTOR
XPATH = By.XPATH

loc_text_boxes = {
    'css': {
        'full_name_input': (CSS, 'input#userName'),
        'email_input': (CSS, 'input#userEmail'),
        'curr_addr_input': (CSS, 'textarea#currentAddress'),
        'perm_addr_input': (CSS, 'textarea#permanentAddress'),
        'submit_button': (CSS, 'button#submit'),
    },
    'xpath': {
        'full_name_input': (XPATH, '//input[@id="userName"]'),
        'email_input': (XPATH, '//input[@id="userEmail"]'),
        'curr_addr_input': (XPATH, '//textarea[@id="currentAddress"]'),
        'perm_addr_input': (XPATH, '//textarea[@id="permanentAddress"]'),
        'submit_button': (XPATH, '//button[@id="submit"]'),
    }}

loc_result_table = {
    'full_name': (CSS, 'p#name'),
    'email': (CSS, 'p#email'),
    'curr_addr': (CSS, 'p#currentAddress'),
    'perm_addr': (CSS, 'p#permanentAddress'),
}
