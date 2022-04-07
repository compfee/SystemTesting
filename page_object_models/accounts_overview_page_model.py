
from tests.config import Config
from utils.driver import Driver
from element_object_models.element import Element

from page_object_models.base_page_model import BasePageModel
from expected_results.page_content.accounts_overview_page_content import AccountsOverviewPageContent
from page_locators.accounts_overview_page_locator import AccountsOverviewPageLocator


class AccountsOverviewPageModel(BasePageModel):


	# _url = OverviewPageContent.URL

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		_url = config.base_url + AccountsOverviewPageContent.URL

	def total_balance(self):

		element = Element(driver=self.driver,
		                  explicit_wait_time=self.explicit_wait_time,
		                  locator=AccountsOverviewPageLocator.TOTAL_VALUE)

		txt = element.text
		return txt


