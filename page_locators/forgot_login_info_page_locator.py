
from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator
from page_locators.base_personal_info_page_locator import BasePersonalInfoPageLocator


class ForgotLoginInfoPageLocator(BasePageLocator, BasePersonalInfoPageLocator):

	FIND_MY_LOGIN_INFO_BUTTON = (By.XPATH,
	                             '//input[contains(@value, "Find My Login Info")]')

	# USERNAME = (By.XPATH, '//*[contains(@b, "Username:")]')
	# PASSWORD = (By.XPATH, '//*[contains(@b, "Password:")]')

	USERNAME_PASSWORD = (By.XPATH, '//*[@id="rightPanel"]/p[2]')

	ERROR_TITLE = (By.XPATH, '//*[@id="rightPanel"]/h1')

	ERROR_MESSAGE = (By.XPATH, '//*[@id="rightPanel"]/p')

