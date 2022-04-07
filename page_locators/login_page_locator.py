
from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class LoginPageLocator(BasePageLocator):

	ERROR_TITLE = (By.XPATH, '//*[@id="rightPanel"]/h1')
	ERROR_MESSAGE = (By.XPATH, '//*[@id="rightPanel"]/p')
