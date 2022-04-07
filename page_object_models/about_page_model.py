
from tests.config import Config
from utils.driver import Driver

from element_object_models.element import Element
from page_object_models.base_page_model import BasePageModel
from page_locators.about_page_locator import AboutPageLocator
from expected_results.page_content.about_page_content import AboutPageContent


class AboutPageModel(BasePageModel):

	# _url = AboutPageContent.URL

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		self._url = config.base_url + AboutPageContent.URL

	# @property
	def description_title(self):

		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.DESCRIPTION_TITLE)
		txt = element.text
		return txt

	# @property
	def description_first_line(self):

		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.FIRST_LINE)
		txt = element.text
		return txt

	# @property
	def description_second_line(self):

		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.SECOND_LINE)
		txt = element.text
		return txt

	# @property
	def description_third_line(self):

		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.THIRD_LINE)
		txt = element.text
		return txt

	# @property
	def description_link(self):

		element = Element(self.driver, self.explicit_wait_time, AboutPageLocator.LINK)
		href = element.element_href
		return href

