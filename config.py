import os

import pydantic_settings
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    context: str = 'remote'
    browser: str = 'chrome'
    browser_version: str = '100'
    browser_timeout: float = 4.0
    mobile_timeout: float = 10.0


config = Config()


def set_browser_options():
    if config.browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920,1080')

    browser.config.base_url = 'https://www.wikipedia.org/'

    if config.context == 'remote':
        load_dotenv()
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        if config.browser == 'firefox' and config.browser_version not in ['97', '98']:
            raise ValueError('This browser version not supported. Available versions: 97, 98')
        if config.browser == 'chrome' and config.browser_version not in ['99', '100']:
            raise ValueError('This browser version not supported. Available version: 99, 100')

        selenoid_capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browser_version,
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        browser.config.driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options
        )
    else:
        browser.config.driver_options = options

    return browser
