
from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator
from expected_results.page_content.account_overview_content import AccountOverviewContent


class AccountsOverviewPageLocator(BasePageLocator):

	HEADER = (By.XPATH, '//h1[@innertext=\'{}\']'.format(AccountOverviewContent.HEADER))

	TOTAL_VALUE = (By.XPATH, '//b[contains(text(), \'$\')]')
