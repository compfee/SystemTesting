
from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator


class AboutPageLocator(BasePageLocator):

	DESCRIPTION_TITLE = (By.XPATH, '//*[@id="rightPanel"]/h1')

	FIRST_LINE = (By.XPATH, '//*[@id="rightPanel"]/p[1]')

	SECOND_LINE = (By.XPATH, '//*[@id="rightPanel"]/p[2]')

	THIRD_LINE = (By.XPATH, '//*[@id="rightPanel"]/p[3]')

	LINK = (By.XPATH, '//*[@id="rightPanel"]/p[3]/a')

