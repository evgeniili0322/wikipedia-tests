from allure import step
from selene import browser, be, have


class MainPage:
    @step('Assert main page title texts')
    def assert_main_page_title_texts(self):
        browser.element('.central-textlogo-wrapper .central-textlogo__image').should(have.exact_text('Wikipedia'))
        browser.element('.central-textlogo-wrapper .localized-slogan').should(have.exact_text('The Free Encyclopedia'))

    @step('Click language list button')
    def click_language_list_button(self):
        browser.element('#js-lang-list-button').click()

    @step('Assert language list')
    def assert_language_list(self):
        browser.element('#js-lang-lists').should(be.visible).should(have.text('1 000 000+ articles'))

    @step('Open mobile application page')
    def open_mobile_application_page(self):
        browser.element('.app-badges strong').click()

    @step('Assert opened mobile application page')
    def assert_opened_mobile_application_page(self):
        browser.element('.mw-page-title-main').should(have.exact_text('List of Wikipedia mobile applications'))

    @step('Open Wiktionary page')
    def open_wiktionary_page(self):
        browser.element('[data-jsl10n="wiktionary.name"]').click()

    @step('Assert opened Wiktionary page')
    def assert_opened_wiktionary_page(self):
        browser.element('.central-textlogo-wrapper .central-textlogo').should(have.exact_text('Wiktionary'))
