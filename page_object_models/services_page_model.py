
from tests.config import Config
from utils.driver import Driver

from page_object_models.base_page_model import BasePageModel
from expected_results.page_content.services_page_content import ServicesPageContent


class ServicesPageModel(BasePageModel):
	'''
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	# _url = ServicesPageContent.URL

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)
		self._url = config.base_url + ServicesPageContent.URL

