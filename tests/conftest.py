import pytest
from selene import browser
from selenium import webdriver

from wikipedia_tests.utils import attach


@pytest.fixture(scope='function')
def browser_opt():
    options = webdriver.ChromeOptions()

    browser.config.base_url = 'https://www.wikipedia.org/'
    options.add_argument('window-size=1920,1080')

    browser.config.driver_options = options

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

# import os
# import pytest
#
# from selene import browser
# from selenium import webdriver
#
# from wikipedia_tests.utils import attach

# options = webdriver.ChromeOptions()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def browser_opt():
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#
#     selenoid_capabilities = {
#         'browserName': 'chrome',
#         'browserVersion': '100',
#         'selenoid:options': {
#             'enableVNC': True,
#             'enableVideo': True
#         }
#     }
#
#     browser.config.base_url = 'https://www.wikipedia.org/'
#     options.add_argument('window-size=1920,1080')
#     options.capabilities.update(selenoid_capabilities)
#
#     browser.config.driver = webdriver.Remote(
#         command_executor='https://user1:1234@selenoid.autotests.cloud/wd/hub',
#         options=options
#     )
#
#     yield browser
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#
#     browser.quit()
