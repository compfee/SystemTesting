
import allure

from tests.config import Config
from utils.driver import Driver
from utils.refresh_page import refresh_page
from utils.http_status_code import get_http_status_code


def open_web_browser(config: Config, page_model, page_content):

	# Open web page
	with allure.step("Open following web page: {}.".format(page_content.URL)):
		driver = Driver(config=config, is_debug=True)
		print('\nbase_url: {}\n'.format(config.base_url))
		page = page_model(config=config, driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		page.go()
		get_http_status_code(page.url())
		refresh_page(page_content.TITLE, page)
		return page
