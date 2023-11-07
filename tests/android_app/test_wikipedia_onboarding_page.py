import allure
import pytest
from allure_commons.types import Severity

from wikipedia_tests.pages.app.android_app import AndroidApp


pytestmark = pytest.mark.usefixtures("android_driver_options")

app = AndroidApp()


@allure.tag('Android app')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Onboarding screen')
@allure.title('Verify onboarding screen')
@allure.link('https://www.wikipedia.org/ ')
def test_onboarding_screen_title_texts():
    app.verify_first_page_title()
    app.verify_second_page_title()
    app.verify_third_page_title()
    app.verify_fourth_page_title()
