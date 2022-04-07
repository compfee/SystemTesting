
from element_object_models.base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
	InvalidElementStateException, \
	NoSuchAttributeException


class Element(BaseElement):

	@property
	def element_src(self):

		src = self.attribute('src')
		return src

	@property
	def element_class(self):

		cls = self.attribute('class')
		return cls

	@property
	def element_alt(self):

		alt = self.attribute('alt')
		return alt

	@property
	def element_title(self):

		alt = self.attribute('title')
		return alt

	@property
	def element_href(self):

		href = self.attribute('href')
		return href

	@property
	def element_type(self):

		atr = self.attribute('type')
		return atr

	@property
	def element_name(self):

		atr = self.attribute('name')
		return atr

	@property
	def element_value(self):

		atr = self.attribute('value')
		return atr

	@property
	def element_target(self):

		atr = self.attribute('target')
		return atr

	@property
	def text(self):

		try:
			text = self.element.text
			return text

		except TimeoutException:
			raise NoSuchAttributeException(
				'\nERROR: The element has no attribute "text".\n'
				'LOCATOR: {}\n'.format(self.locator))

	def click_on(self):

		try:
			element = WebDriverWait(self.driver,
			                        self.explicit_wait_time).until(EC.element_to_be_clickable(self.locator))
			element.click()
			return None

		except TimeoutException:
			raise InvalidElementStateException(
				'\nERROR: can not find element. The element is invisible or not clickable.\n')

	def is_visible(self):

		try:
			element = WebDriverWait(self.driver,
			                        self.explicit_wait_time).until(EC.visibility_of_element_located(self.locator))
			return True
		except TimeoutException:
			return False

	def write(self, text):

		self.element.clear()
		self.element.send_keys(text)
		return None
