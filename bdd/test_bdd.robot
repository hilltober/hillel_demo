*** Settings ***
Documentation   This is a simple test case
Library         SeleniumLibrary
Library         ./chromedriver.py

*** Variables ***
${PAGE_URL}             https://www.google.com/
${BUTTON_FIND}          name=btnK
${FIELD_SEARCH}         name=q
${KEYWORD}              Robot Framework

*** Test Cases ***
Example Test
    [Documentation]  Example test.
    [Tags]  Smoke
    ${chromedriver_path}            get_chromedriver_path
    Create Webdriver    Chrome      executable_path=${chromedriver_path}

    Go To  ${PAGE_URL}
    Input Text  ${FIELD_SEARCH}     ${KEYWORD}
    Wait until element is visible   ${BUTTON_FIND}
    Click Button                    ${BUTTON_FIND}
    Wait until page contains        ${KEYWORD}
    Close Browser
