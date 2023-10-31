import os

import pydantic_settings
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options


class Config(pydantic_settings.BaseSettings):
    web_context: str = 'remote'
    app_context: str = 'bstack'
    browser: str = 'chrome'
    browser_version: str = '100'
    browser_timeout: float = 4.0
    mobile_timeout: float = 10.0


config = Config()

if config.app_context == 'bstack' or config.web_context == 'remote':
    load_dotenv()


def set_browser_options():
    if config.browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920,1080')

    browser.config.base_url = 'https://www.wikipedia.org/'
    browser.config.timeout = config.browser_timeout

    if config.web_context == 'remote':
        login = os.getenv('SELENOID_LOGIN')
        password = os.getenv('SELENOID_PASSWORD')

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


def set_android_driver_options():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'appWaitActivity': 'org.wikipedia.*',
        "appium:disableIdLocatorAutocompletion": True
    })

    if config.app_context == 'bstack':
        load_dotenv('.env.bstack')
        options.set_capability('app', os.getenv('APP_ID'))
        options.set_capability(
            "bstack:options", {
                "userName": os.getenv('BS_USER_NAME'),
                "accessKey": os.getenv('BS_ACCESS_KEY'),
                'platformVersion': '9.0',
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                'deviceName': os.getenv('DEVICE_NAME')
            },
        )

    if config.app_context.startswith('local'):
        apk_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'wikipedia_tests', 'resources', 'apk', 'app-alpha-universal-release.apk')

        if config.app_context == 'local_emulator':
            load_dotenv('.env.local_emulator')
        else:
            load_dotenv('.env.local_real')

        options.set_capability('app', apk_path)
        options.set_capability('udid', os.getenv('UDID'))

    return options
