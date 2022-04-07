
from tests.config import Config
from utils.driver import Driver
from element_object_models.element import Element

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_locators.base_page_locator import BasePageLocator
from expected_results.page_content.base_page_content import BasePageContent
from page_locators.account_services_menu_locator import AccountServicesMenuLocator
from expected_results.page_content.login_page_content import LoginPageContent
from expected_results.page_content.accounts_overview_page_content import AccountsOverviewPageContent


class BasePageModel:

	# _url = BasePageContent.URL

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		self._config = config
		self._url = config.base_url + BasePageContent.URL
		self._implicit_wait_time = implicit_wait_time
		self._explicit_wait_time = explicit_wait_time
		self._driver = self._set_driver(driver)
		self._set_implicit_wait(implicit_wait_time)
		self._explicit_wait_time = self._set_explicit_wait(explicit_wait_time)

	@property
	def config(self):
		return self._config

	@property
	def implicit_wait_time(self):
		return self._implicit_wait_time

	@property
	def explicit_wait_time(self):
		return self._explicit_wait_time

	@staticmethod
	def _set_driver(driver):

		# print('\nDriver type: {}'.format(type(driver)))  # debug only
		if isinstance(driver, Driver):
			return driver.get_driver()

		return driver

	def _set_implicit_wait(self, implicit_wait_time: int):

		if type(implicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. Please set "implicit_wait_time" value as integer.\n')
		self._driver.implicitly_wait(implicit_wait_time)
		return None

	@staticmethod
	def _set_explicit_wait(explicit_wait_time: int):

		if type(explicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. Please set "explicit_wait_time" value as integer.\n')
		return explicit_wait_time

	@property
	def explicit_wait_time(self):
		return self._explicit_wait_time

	@property
	def implicit_wait_time(self):
		return self._implicit_wait_time

	def go(self):

		self._driver.get(self._url)
		self._driver.maximize_window()
		return None

	def quit(self):

		if self._driver:
			self._driver.quit()
		return None

	def close(self):

		if self._driver:
			self._driver.close()
		return None

	@property
	def driver(self):

		return self._driver

	# @property
	def title(self):

		return self._driver.title

	# @property
	def url(self):

		url = self._driver.current_url

		if ';' in url:
			url = url[:url.index(';')]

		if '?ConnType=JDBC' in url:
			url = url[:url.index('?ConnType=JDBC')]

		return url

	# @property
	def slogan(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SLOGAN)
		return element.text

	@staticmethod
	def _formated_url(url: str):

		url = url.replace(BasePageContent.URL, '')

		if ';' in url:
			if '?_wadl&_type=xml' in url:
				url = url[:url.index(';')] + '?_wadl&_type=xml'
			else:
				url = url[:url.index(';')]

		return url

	# @property
	def admin_logo_formated_href(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_HREF)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def admin_logo_formated_img_src(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_IMG)
		src = self._formated_url(element.element_src)
		return src

	# @property
	def admin_logo_img_class(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_LOGO_IMG)
		return element.element_class

	# @property
	def para_bank_logo_formated_href(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_HREF)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def para_bank_logo_formated_img_src(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		src = self._formated_url(element.element_src)
		return src

	# @property
	def para_bank_logo_img_class(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_class

	# @property
	def para_bank_logo_img_alt(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_alt

	# @property
	def para_bank_logo_img_title(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PARA_BANK_LOGO_IMG)
		return element.element_title

	# @property
	def home_button_formated_href(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.HOME_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def home_button_text(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.HOME_BUTTON)
		return element.text

	# @property
	def about_button_formated_href(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def about_button_text(self):

		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		return element.text

	# @property
	def contact_button_formated_href(self):
		'''
		Returns formated contact button href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CONTACT_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def contact_button_text(self):
		'''
		Returns contact button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CONTACT_BUTTON)
		return element.text

	# @property
	def solutions_menu_text(self):
		'''
		Returns SOLUTIONS button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SOLUTIONS)
		return element.text

	# @property
	def solutions_menu_class(self):
		'''
		Returns SOLUTIONS button text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SOLUTIONS)
		return element.element_class

	# @property
	def about_us_menu_item_formated_href(self):
		'''
		Returns formated about us menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_BUTTON)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def about_us_menu_item_text(self):
		'''
		Returns about us menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ABOUT_US_MENU_ITEM)
		return element.text

	# @property
	def services_us_menu_item_formated_href(self):
		'''
		Returns formated services menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SERVICES_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def services_us_menu_item_text(self):
		'''
		Returns services menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.SERVICES_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def products_menu_item_formated_href(self):
		'''
		Returns formated products menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PRODUCTS_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def products_menu_item_text(self):
		'''
		Returns products menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PRODUCTS_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def locations_menu_item_formated_href(self):
		'''
		Returns formated locations menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOCATIONS_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def locations_menu_item_text(self):
		'''
		Returns locations menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOCATIONS_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def admin_page_menu_item_formated_href(self):
		'''
		Returns formated admin_page menu item href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_PAGE_MENU_ITEM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def admin_page_menu_item_text(self):
		'''
		Returns admin_page menu item text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ADMIN_PAGE_MENU_ITEM)
		txt = element.text
		return txt

	# @property
	def customer_login_title(self):
		'''
		Returns customer login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_TITLE)
		txt = element.text
		return txt

	# @property
	def username_login_title(self):
		'''
		Returns username login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.USERNAME_LOGIN_TITLE)
		txt = element.text
		return txt

	# @property
	def password_login_title(self):
		'''
		Returns password login title
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.PASSWORD_LOGIN_TITLE)
		txt = element.text
		return txt

	# @property
	def username_input_class(self):
		'''
		Returns Username login Input class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_class
		return atr

	# @property
	def username(self):
		'''
		Returns Username value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		value = element.element_value
		return value

	# @property
	def username_input_type(self):
		'''
		Returns Username login Input type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_type
		return atr

	def enter_username(self, username):
		'''
		Type username into Username input field
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		element.write(username)
		return None

	# @property
	def username_input_name(self):
		'''
		Returns Username login Input name
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_USERNAME_INPUT)
		atr = element.element_name
		return atr

	# @property
	def password(self):
		'''
		Returns Password value
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		value = element.element_value
		return value

	# @property
	def password_input_class(self):
		'''
		Returns password login Input class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_class
		return atr

	# @property
	def password_input_type(self):
		'''
		Returns password login Input type
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_type
		return atr

	# @property
	def password_input_name(self):
		'''
		Returns password login Input name
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		atr = element.element_name
		return atr

	def enter_password(self, password):
		'''
		Type password into Password input field
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.LOGIN_PASSWORD_INPUT)
		element.write(password)
		return None

	# @property
	def login_button_class(self):
		'''
		Returns login_button class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_class
		return atr

	# @property
	def login_button_type(self):
		"""
		Returns login_button type
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_type
		return atr

	# @property
	def login_button_value(self):
		"""
		Returns login_button value
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		atr = element.element_value
		return atr

	def hit_login_button(self):
		"""
		1. Click on Log In button
		2. Wait until URL changes
		3. Returns OverviewPageModel object on success
		4. Return TimeOut exception on failure
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.CUSTOMER_LOGIN_BUTTON)
		current_url = self.url()
		element.click_on()
		WebDriverWait(self.driver, self.explicit_wait_time).until(EC.url_changes(current_url))

		if self.url() == self.config.base_url + AccountsOverviewPageContent.URL:
			from page_object_models.accounts_overview_page_model import AccountsOverviewPageModel
			return AccountsOverviewPageModel(config=self.config,
			                                 driver=self.driver,
			                                 implicit_wait_time=5,
			                                 explicit_wait_time=10)

		if self.url() == self.config.base_url + LoginPageContent.URL:
			from page_object_models.login_page_model import LoginPageModel
			return LoginPageModel(config=self.config,
			                      driver=self.driver,
			                      implicit_wait_time=5,
			                      explicit_wait_time=10)

		raise Exception("Unknown URL: {} > Flow is not implemented".format(self.driver.current_url))

	# @property
	def forgot_login_formated_href(self):
		"""
		Returns formated forgot_login href
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FORGOT_LOGIN)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def forgot_login_text(self):
		"""
		Returns forgot_login text
		:return:
		"""
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FORGOT_LOGIN)
		txt = element.text
		return txt

	# @property
	def register_formated_href(self):
		'''
		Returns formated register href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.REGISTER)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def register_text(self):
		'''
		Returns register text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.REGISTER)
		txt = element.text
		return txt

	# @property
	def footer_home_formated_href(self):
		'''
		Returns formated footer_home href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_HOME)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_home_text(self):
		'''
		Returns footer_home text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_HOME)
		txt = element.text
		return txt

	# @property
	def footer_about_us_formated_href(self):
		'''
		Returns formated about_us href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_ABOUT_US)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_about_us_text(self):
		'''
		Returns about_us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_ABOUT_US)
		txt = element.text
		return txt

	# @property
	def footer_services_formated_href(self):
		'''
		Returns formated services href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SERVICES)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_services_text(self):
		'''
		Returns services text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SERVICES)
		txt = element.text
		return txt

	# @property
	def footer_products_formated_href(self):
		'''
		Returns formated products href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_PRODUCTS)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_products_text(self):
		'''
		Returns products text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_PRODUCTS)
		txt = element.text
		return txt

	# @property
	def footer_locations_formated_href(self):
		'''
		Returns formated locations href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_LOCATIONS)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_locations_text(self):
		'''
		Returns products text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_LOCATIONS)
		txt = element.text
		return txt

	# @property
	def footer_forum_formated_href(self):
		'''
		Returns formated forum href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_FORUM)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_forum_text(self):
		'''
		Returns forum text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_FORUM)
		txt = element.text
		return txt

	# @property
	def footer_site_map_formated_href(self):
		'''
		Returns formated site_map href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SITE_MAP)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_site_map_text(self):
		'''
		Returns site_map text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_SITE_MAP)
		txt = element.text
		return txt

	# @property
	def footer_contact_us_formated_href(self):
		'''
		Returns formated contact_us href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_CONTACT_US)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_contact_us_text(self):
		'''
		Returns contact_us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_CONTACT_US)
		txt = element.text
		return txt

	# @property
	def footer_copyright_text(self):
		'''
		Returns copyright text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_COPYRIGHT)
		txt = element.text
		return txt

	# @property
	def footer_copyright_class(self):
		'''
		Returns copyright class
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_COPYRIGHT)
		atr = element.element_class
		return atr

	# @property
	def footer_visit_link_formated_href(self):
		'''
		Returns formated visit link href
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US_LINK)
		href = self._formated_url(element.element_href)
		return href

	# @property
	def footer_visit_link_text(self):
		'''
		Returns visit link text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US_LINK)
		txt = element.text
		return txt

	# @property
	def footer_visit_link_target(self):
		'''
		Returns visit us target
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US_LINK)
		atr = element.element_target
		return atr

	# @property
	def footer_visit_us_text(self):
		'''
		Returns visit us text
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.FOOTER_VISIT_US)
		txt = element.text
		return txt

	# Account Services Menu - visible only when user logged in
	# @property
	def welcome_message(self):
		'''
		Returns 'welcome' message that appears above "Account Services" menu
		:param user:
		:return:
		'''

		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.WELCOME_MESSAGE)
		txt = element.text
		return txt

	# @property
	def account_services_menu_title(self):
		'''
		Returns "Account Services" menu header
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNT_SERVICES_HEADER)
		txt = element.text
		return txt

	# @property
	def account_services_menu_is_visible(self):
		'''
		Returns is "Account Services" menu header visible
		:return:
		'''
		try:
			element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNT_SERVICES_HEADER)
			is_visible = element.is_visible()
			return is_visible
		except NoSuchElementException:
			return False

	def open_new_account(self):
		'''
		Click on "Open New Account"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.OPEN_NEW_ACCOUNT)
		element.click_on()
		return None

	def accounts_overview(self):
		'''
		Click on "Account Overview"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.ACCOUNTS_OVERVIEW)
		element.click_on()
		return None

	def transfer_funds(self):
		'''
		Click on "Transfer Funds"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.TRANSFER_FUNDS)
		element.click_on()
		return None

	def bill_pay(self):
		'''
		Click on "Bill Pay"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.BILL_PAY)
		element.click_on()
		return None

	def find_transactions(self):
		'''
		Click on "Find Transactions"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.FIND_TRANSACTIONS)
		element.click_on()
		return None

	def update_contact_info(self):
		'''
		Click on "Update Contact Info"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.UPDATE_CONTACT_INFO)
		element.click_on()
		return None

	def request_loan(self):
		'''
		Click on "Request Loan"
		:return:
		'''
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.REQUEST_LOAN)
		element.click_on()
		return None

	def hit_log_out_button(self):
		'''
		1. Click on "Log Out"
		2. Wait until URL changes
		3. Returns HomePageModel on success
		4. Return TimeoutException on failure

		An expectation for checking the current url.
        url is the expected url, which must not be an exact match
        returns True if the url is different, false otherwise.

        Source: https://seleniumhq.github.io/selenium/docs/api/py/_modules/selenium/webdriver/support/expected_conditions.html#url_changes
		:return:
		'''

		current_url = self.driver.current_url
		element = Element(self.driver, self.explicit_wait_time, AccountServicesMenuLocator.LOG_OUT)
		element.click_on()
		WebDriverWait(self.driver, self.explicit_wait_time).until(EC.url_changes(current_url))
		from page_object_models.home_page_model import HomePageModel
		return HomePageModel(config=self.config,
		                     driver=self.driver,
		                     implicit_wait_time=5,
		                     explicit_wait_time=10)

	def hit_bill_pay(self):
		"""
		Press on "Bill Pay" menu item
		Returns "Bill Payment Service" page object on success

		:return:
		"""
		current_url = self.driver.current_url
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.BILL_PAY)
		element.click_on()
		WebDriverWait(self.driver, self.explicit_wait_time).until(EC.url_changes(current_url))
		from page_object_models.bill_pay_page_model import BillPayPageModel
		return BillPayPageModel(config=self.config,
		                        driver=self.driver,
		                        implicit_wait_time=self.implicit_wait_time,
		                        explicit_wait_time=10)

	def hit_accounts_overview(self):
		"""
		Press on "Accounts Overview" menu item
		Returns "Accounts Overview" page object on success

		:return:

		"""
		current_url = self.driver.current_url
		element = Element(self.driver, self.explicit_wait_time, BasePageLocator.ACCOUNTS_OVERVIEW)
		element.click_on()
		WebDriverWait(self.driver, self.explicit_wait_time).until(EC.url_changes(current_url))
		from page_object_models.accounts_overview_page_model import AccountsOverviewPageModel
		return AccountsOverviewPageModel(config=self.config,
		                                 driver=self.driver,
		                                 implicit_wait_time=self.implicit_wait_time,
		                                 explicit_wait_time=10)


