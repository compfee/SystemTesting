
from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class AdminPageLocator(BasePageLocator):

	INITIALIZE_BUTTON = (By.XPATH, '//button[contains(text(),\'Initialize\')]')

	CLEAN_BUTTON = (By.XPATH, '//button[contains(text(),\'Clean\')]')
