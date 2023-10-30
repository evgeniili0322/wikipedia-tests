from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class AndroidApp:
    search_results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
    onboarding_continue_button = browser.element((AppiumBy.ID,
                                                  'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
    onboarding_page_title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    @step('Skip wellcome screen')
    def skip_welcome_screen(self):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    @step('Type search')
    def type_search(self, value):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(value)

    @step('Verify found content')
    def verify_found_article(self, value):
        self.search_results.should(have.size_greater_than(0))
        self.search_results.first.should(have.text(value))

    @step('Open article page')
    def open_article_page(self):
        self.search_results.first.click()

    @step('Verify opened article')
    def verify_opened_article(self, value):
        browser.element((AppiumBy.XPATH, f'(//android.widget.TextView[@text="{value}"])[1]')).should(be.visible)

    @step('Verify first page')
    def verify_first_page_title(self):
        self.onboarding_page_title.should(have.text('The Free Encyclopedia'))
        self.onboarding_continue_button.click()

    @step('Verify second page')
    def verify_second_page_title(self):
        self.onboarding_page_title.should(have.text('New ways to explore'))
        self.onboarding_continue_button.click()

    @step('Verify third page')
    def verify_third_page_title(self):
        self.onboarding_page_title.should(have.text('Reading lists with sync'))
        self.onboarding_continue_button.click()

    @step('Verify fourth page')
    def verify_fourth_page_title(self):
        self.onboarding_page_title.should(have.text('Send anonymous data'))
