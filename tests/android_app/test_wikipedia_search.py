import allure
import pytest
from allure_commons.types import Severity

from wikipedia_tests.pages.app.android_app import AndroidApp
from wikipedia_tests.data.search_query import search_query


pytestmark = pytest.mark.usefixtures("android_driver_options")

app = AndroidApp()


@allure.tag('Android app')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Search')
@allure.story('Verify found article')
@allure.link('https://www.wikipedia.org/ ')
def test_found_articles():
    app.skip_welcome_screen()
    app.type_search(search_query.multiple_articles)

    app.verify_found_article(search_query.multiple_articles)


@allure.tag('Android app')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Search')
@allure.story('Open article page')
@allure.link('https://www.wikipedia.org/ ')
def test_open_found_article():
    app.skip_welcome_screen()
    app.type_search(search_query.multiple_articles)
    app.open_article_page()

    app.verify_opened_article(search_query.multiple_articles)
