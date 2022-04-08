
import os
import platform

from selenium import webdriver

from tests.config import Config
from utils.path_config import DriverPath
from selenium.common.exceptions import WebDriverException


class Driver:

    _driver_path = {

        'chrome': DriverPath.CHROME_WEB_DRIVER_PATH,
        'mozilla': DriverPath.MOZILLA_WEB_DRIVER_PATH,
        'edge': DriverPath.EDGE_WEB_DRIVER_PATH
    }

    def __init__(self, config: Config, is_debug=False):
        self._config = config
        self._is_debug = is_debug
        self._browser = self._config.browser
        self._driver = self._set_driver()

    def _set_driver(self):

        driver = None

        if self._browser == 'chrome':
            try:
                if self._config.is_headless:
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('headless')
                    driver = webdriver.Chrome(options=chrome_options)
                else:
                    driver = webdriver.Chrome()

            except WebDriverException as e:
                if self._is_debug:
                    print('\nPlease note: \n', e)

                path = self._get_driver_path()

                if self._is_debug:
                    print('\nTrying to look for a \'chromedriver\' under:\n{}'.format(path))

                driver = webdriver.Chrome(executable_path=path)

        if self._browser == 'mozilla':
            try:
                if self._config.is_headless:
                    # Set the MOZ_HEADLESS environment variable which casues Firefox to start in headless mode.
                    # Source: https://intoli.com/blog/running-selenium-with-headless-firefox/
                    os.environ['MOZ_HEADLESS'] = '1'
                    driver = webdriver.Firefox()
                else:
                    driver = webdriver.Firefox()

            except WebDriverException as e:
                if self._is_debug:
                    print('\nPlease note:', e.msg)
                path = self._get_driver_path()
                if self._is_debug:
                    print('\nTrying to look for a \'geckodriver\' under:\n{}'.format(path))
                driver = webdriver.Firefox(executable_path=path)

        if self._browser == 'edge':
            '''
            Purpose:	Probe the underlying platform’s hardware, operating system,
            and interpreter version information.

            print('Version tuple:', platform.python_version_tuple())
            print('Compiler     :', platform.python_compiler())
            print('Build        :', platform.python_build())
            '''

            if sum(int(i) for i in platform.python_version_tuple()) > 13:
                if self._is_debug:
                    print('\nVersion:', platform.python_version())
                    print('WebDriver is now a Feature On Demand')
                    print('For more info please check: {}'.format(
                        'https://blogs.windows.com/msedgedev/2018/06/14/'
                        'webdriver-w3c-recommendation-feature-on-demand/#Rg8g2hRfjBQQVRXy.97\n'))
                driver = webdriver.Edge()
            else:
                path = self._get_driver_path()
                if self._is_debug:
                    print('\nTrying to look for a \'MicrosoftWebDriver\' under:\n{}'.format(path))
                driver = webdriver.Edge(executable_path=path)

        return driver

    def _get_root_dir(self):
        root_dir = os.path.dirname(os.path.realpath(__file__)).split('\\')
        dir_list = [str(i) for i in root_dir]
        root_dir_index = dir_list.index("ParaBankSeleniumAutomation")
        root = '\\'.join(root_dir[:root_dir_index + 1])
        if self._is_debug:
            print('ROOT DIR:\n', root)
        return root

    def _get_driver_path(self):
        #return self._get_root_dir() + self._driver_path[self._browser]
        return 'G:\Polikek\maslakov\сайтик\chromedriver.exe'

    def get_driver(self):
        return self._driver

    def get_browser(self):
        return self._browser
