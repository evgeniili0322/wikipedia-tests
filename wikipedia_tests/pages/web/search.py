from allure import step
from selene import browser, have


class Search:
    @step('Type search')
    def type_search(self, value):
        browser.element('input#searchInput').type(value).press_enter()

    @step('Assert found article')
    def assert_found_article(self, value):
        browser.element('caption.infobox-title').should(have.text(value))

    @step('Assert found multiple articles')
    def assert_found_multiple_articles(self, value):
        browser.element('div.mw-parser-output > p').should(have.text(f'{value} may refer to:'))

    @step('Assert no matching results')
    def assert_no_matching_results(self):
        browser.element('.mw-search-nonefound').should(have.exact_text('There were no results matching the query.'))
