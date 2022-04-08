
import allure
import pytest

from tests.config import Config
from utils.clean_database import clean_database
from utils.get_args_from_cli import get_args
from utils.screenshot import screenshot_on_fail
from utils.step_definition import step_definition
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.invalid_users_templates.invalid_data import InvalidData

from page_object_models.register_page_model import RegisterPageModel
from tests.e2e_tests.base_case.user_registration_case import UserRegistrationCase
from expected_results.page_content.register_page_content import RegisterPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Registration")
@allure.sub_suite('Negative Tests')
@allure.feature("Register Page")
@allure.story('Register Functionality')
@pytest.mark.skipif(get_args()['env'] == 'production',
                    reason="This is demo test that will have negative effect on Travis CI status")
@screenshot_on_fail()
class TestUserRegistrationInvalidData(UserRegistrationCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(InvalidData)
		cls.page = None
		cls.config = Config()

		with allure.step("Initial data setup > clean DB"):
			clean_database(cls.config)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}".format(RegisterPageContent.URL)):
			self.page_model = RegisterPageModel
			self.page_context = RegisterPageContent
			with allure.step("Open web browser"):
				self.page = open_web_browser(config=self.config,
				                             page_model=self.page_model,
				                             page_content=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_user_registration(self):
		allure.dynamic.description("""
		User registration test case:
			1. Open 'Register' web page
			2. Fill out user personal data > Set all fields with invalid data
			3. Verify that each data item (invalid data string) appears in relevant field
			4. Hit 'Register' button
			5. Verify 'Error' messages
			6. Verify that "Account Services" menu is not present
			7. Close web browser
		""")
		allure.dynamic.title("User registration > Negative test > Invalid data")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.fill_out_user_data()

		'''
		step_definition(self,
		                step_description='Hit "Register" button',
		                expected=True,
		                actual=True,
		                act=self.page.hit_register_btn,
		                click=True)
		'''
		with allure.step('Hit "Register" button'):
			print('Hit "Register" button')
			self.page = self.page.hit_register_btn()

		# step_definition(self,
		#                 step_description='Verify that "Account Services" menu is not present',
		#                 expected=False,
		#                 actual=self.page.account_services_menu_is_visible,
		#                 act=None,
		#                 click=False)

		self.verify_first_name_error()

		self.verify_last_name_error()

		self.verify_address_error()

		self.verify_city_error()

		self.verify_state_error()

		self.verify_zip_code_error()

		self.verify_ssn_error()
