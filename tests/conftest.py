import allure_commons
import pytest
from selene import support

from config import set_browser_options, config
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
    if config.context == 'remote':
        attach.add_video(browser)

    browser.quit()
