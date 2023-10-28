import allure
import pytest
from allure_commons.types import Severity

from wikipedia_tests.application import app


pytestmark = pytest.mark.usefixtures("browser_options")


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Assert main page title texts')
@allure.link('https://www.wikipedia.org/ ')
def test_main_page_title_texts():
    app.open()

    app.main_page.assert_main_page_title_texts()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Assert language list')
@allure.link('https://www.wikipedia.org/ ')
def test_languages_list():
    app.open()

    app.main_page.click_language_list_button()

    app.main_page.assert_language_list()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Open mobile application page')
@allure.link('https://www.wikipedia.org/ ')
def test_open_mobile_applications_page():
    app.open()

    app.main_page.open_mobile_application_page()

    app.main_page.assert_opened_mobile_application_page()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Main page')
@allure.story('Open Wiktionary page')
@allure.link('https://www.wikipedia.org/')
def test_open_wiktionary_page():
    app.open()

    app.main_page.open_wiktionary_page()

    app.main_page.assert_opened_wiktionary_page()
