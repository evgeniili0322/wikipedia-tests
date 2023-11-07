import os

import allure_commons
import pytest
from allure import step
from appium import webdriver
from selene import support, browser

from config import set_android_driver_options, set_browser_options, config
from wikipedia_tests.utils import attach


@pytest.fixture(scope='function')
def browser_options():
    browser = set_browser_options()
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield browser

    if config.browser == 'chrome':
        attach.add_logs(browser)

    attach.add_screenshot(browser)
    attach.add_html(browser)

    if config.web_context == 'remote':
        attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def android_driver_options():
    with step('Init app session'):
        browser.config.driver = webdriver.Remote(
            options=set_android_driver_options(),
            command_executor=os.getenv('REMOTE_URL'),
        )

    browser.config.timeout = config.mobile_timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.driver.session_id

    with step('Tear down app session'):
        browser.quit()

    if config.app_context == 'bstack':
        attach.attach_bstack_video(session_id, os.getenv('BS_USER_NAME'), os.getenv('BS_ACCESS_KEY'))

    browser.quit()
