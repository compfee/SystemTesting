
import allure
import unittest
import pytest

from tests.config import Config
from utils.get_args_from_cli import get_args
from utils.register_user import register_user
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition

from expected_results.users.base_user import BaseUser
from page_object_models.about_page_model import AboutPageModel
from expected_results.users.valid_users_templates.jane_doe import JaneDoe
from expected_results.page_content.about_page_content import AboutPageContent
from expected_results.page_content.bank_account_content import BankAccountContent
from expected_results.page_content.home_page_content import HomePageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite("Positive Tests")
@allure.feature("About Page")
@allure.story('Login/Logout Functionality')
@pytest.mark.skipif(get_args()['env'] == 'production',
                    reason="This is demo test that will have negative effect on Travis CI status")
@screenshot_on_fail()
class TestUserLoginFromAboutUsPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = BaseUser(JaneDoe)
        cls.config = Config()
        cls.page_model = AboutPageModel
        cls.page_content = AboutPageContent

        with allure.step("Initial data setup > clean DB"):
            clean_database(config=cls.config)

        with allure.step("Initial data setup > register test user"):
            register_user(cls.user, cls.config)

        with allure.step("Open web browser"):
            cls.page = open_web_browser(config=cls.config,
                                        page_model=cls.page_model,
                                        page_content=cls.page_content)

    @classmethod
    def tearDownClass(cls):
        with allure.step("Close web browser"):
            if cls.page:
                cls.page.quit()
                cls.page = None

    def test_user_login_logout(self):
        allure.dynamic.description("""
                User Log In validation > Login from About Us page:
                    1. Open Home web page
                    2. Do URL verification
                    3. Do Title verification
                    4. Type username/password
                    5. Hit "Log In" button
                    6. Verify "Welcome" message
                    7. Verify that "Account Services" menu is present
                    8. Do URL verification
                    9. Log Out
                    10. Do URL verification
                    11. Verify that "Account Services" menu is not present
                    12. Verify web page title
                    13. Close web browser
                """)
        allure.dynamic.title("About page > User Log In validation > Positive test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        step_definition(self,
                        step_description='Type Username > Verify Username value',
                        expected=self.user.username,
                        actual=self.page.username,
                        act=self.page.enter_username,
                        click=False)

        step_definition(self,
                        step_description='Type Password > Verify Password value',
                        expected=self.user.password,
                        actual=self.page.password,
                        act=self.page.enter_password,
                        click=False)

        with allure.step('Hit Log In button'):
            self.page = self.page.hit_login_button()

        step_definition(self,
                        step_description='Verify "Welcome" message',
                        expected='{}{} {}'.format(BankAccountContent.ACCOUNT_SERVICES_MENU['welcome_message'],
                                                  self.user.first_name,
                                                  self.user.last_name),
                        actual=self.page.welcome_message,
                        act=None,
                        click=False)

        step_definition(self,
                        step_description='Verify that "Account Services" menu is present',
                        expected=True,
                        actual=self.page.account_services_menu_is_visible,
                        act=None,
                        click=False)

        # Log Out
        with allure.step('Hit "Log Out" link'):
            self.page = self.page.hit_log_out_button()

        # Post Logout validation
        step_definition(self,
                        step_description='Do URL verification',
                        expected=self.config.base_url + HomePageContent.URL,
                        actual=self.page.url,
                        act=None,
                        click=False)

        step_definition(self,
                        step_description='Verify that "Account Services" menu is not shown',
                        expected=False,
                        actual=self.page.account_services_menu_is_visible,
                        act=None,
                        click=False)

        # Verify Page Title
        step_definition(self,
                        step_description='Verify web page title',
                        expected=HomePageContent.TITLE,
                        actual=self.page.title,
                        act=None,
                        click=False)
