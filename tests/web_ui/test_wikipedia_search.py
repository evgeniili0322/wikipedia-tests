import allure
import pytest
from allure_commons.types import Severity

from wikipedia_tests.web_application import app
from wikipedia_tests.data.search_query import search_query


pytestmark = pytest.mark.usefixtures("browser_options")


@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Search')
@allure.story('Found article')
@allure.link('https://www.wikipedia.org/ ')
def test_found_article():
    app.open()

    app.search.type_search(search_query.single_article)

    app.search.assert_found_article(search_query.single_article)


@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Search')
@allure.story('Found multiple articles')
@allure.link('https://www.wikipedia.org/ ')
def test_found_multiple_articles():
    app.open()

    app.search.type_search(search_query.multiple_articles)

    app.search.assert_found_multiple_articles(search_query.multiple_articles)


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Search')
@allure.story('No matching results')
@allure.link('https://www.wikipedia.org/ ')
def test_no_matching_results():
    app.open()

    app.search.type_search('Python')

    app.search.assert_no_matching_results()
