
import selenium.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, \
    NoSuchElementException, \
    NoSuchAttributeException


class BaseElement:

    def __init__(self, driver: selenium.webdriver, explicit_wait_time: int, locator=None):
        self._driver = self._set_driver(driver)
        self._explicit_wait_time = explicit_wait_time
        self._locator = self._set_locator(locator)
        self._element = self._find_element()

    @property
    def explicit_wait_time(self):

        return self._explicit_wait_time

    @property
    def driver(self):

        return self._driver

    def attribute(self, attribute: str):

        try:
            atr = self.element.get_attribute(attribute)
            # print('\nattribute: {}, object: {}'.format(attribute, atr))  # debug only
            return atr

        except TimeoutException:
            raise NoSuchAttributeException(
                '\nERROR: The element has no attribute "{}".\n'
                'LOCATOR: {}\n'.format(attribute, self.locator))

    @property
    def element(self):

        return self._element

    @property
    def locator(self):

        return self._locator

    def _find_element(self):

        try:
            element = WebDriverWait(self.driver, self.explicit_wait_time).until(
                EC.presence_of_element_located(self.locator))
            return element

        except TimeoutException:
            raise NoSuchElementException(
                '\nERROR: can not find element. The element is not present on the DOM.\n'
                'LOCATOR: {}\n'.format(self.locator))

    @staticmethod
    def _set_driver(driver: selenium.webdriver):

        BaseElement._check_driver_type(driver)
        return driver

    @staticmethod
    def _check_driver_type(driver):

        # print('\nDRIVER TYPE: {}, {}\n'.format(type(driver),
        # driver.capabilities['browserName']))  # Debug only
        if driver.capabilities['browserName'] == 'chrome':
            if not isinstance(driver, selenium.webdriver.chrome.webdriver.WebDriver):
                raise TypeError('\nERROR: driver must be of type '
                                '"selenium.webdriver.chrome_tests.webdriver.WebDriver"\n')
            return None

        if driver.capabilities['browserName'] == 'firefox':
            if not isinstance(driver, selenium.webdriver.firefox.webdriver.WebDriver):
                raise TypeError('\nERROR: driver must be of type '
                                '"selenium.webdriver.firefox.webdriver.WebDriver"\n')
            return None

        if driver.capabilities['browserName'] == 'MicrosoftEdge':
            if not isinstance(driver, selenium.webdriver.edge.webdriver.WebDriver):
                raise TypeError('\nERROR: driver must be of type '
                                '"selenium.webdriver.edge.webdriver.WebDriver"\n')
            return None

        raise TypeError('\nERROR: unsupported webdriver type: '
                        '{}. Browser: {}\n'.format(type(driver),
                                                   driver.capabilities['browserName']))

    @staticmethod
    def _set_locator(locator: tuple):

        if not isinstance(locator, tuple):
            raise TypeError('\nERROR: locator must be of type TUPLE\n')
        return locator
