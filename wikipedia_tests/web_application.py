from allure import step
from selene import browser

from wikipedia_tests.pages.web.main_page import MainPage
from wikipedia_tests.pages.web.search import Search


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.search = Search()

    @step('Open main page')
    def open(self):
        browser.open('')


app = Application()
