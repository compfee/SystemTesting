
from tests.config import Config
from utils.driver import Driver

from element_object_models.element import Element
from page_object_models.base_page_model import BasePageModel
from page_locators.admin_page_locator import AdminPageLocator
from expected_results.page_content.admin_page_content import AdminPageContent


class AdminPageModel(BasePageModel):


	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		self._url = config.base_url + AdminPageContent.URL

	def hit_initialize_button(self):

		element = Element(self.driver, self.explicit_wait_time, AdminPageLocator.INITIALIZE_BUTTON)
		element.click_on()
		return None

	def hit_clean_button(self):

		element = Element(self.driver, self.explicit_wait_time, AdminPageLocator.CLEAN_BUTTON)
		element.click_on()
		return None
