
from pytest import fixture


def pytest_addoption(parser):

	parser.addoption('--env',
	                 action="store",
	                 help="Base URL/Environment")

	parser.addoption('--browser',
	                 action="store",
	                 help="Web browser name")

	parser.addoption('--is_headless',
	                 action="store",
	                 help="Headless browser run without a UI")


@fixture(scope='session')
def env(request):
	return request.config.getoption("--env")


@fixture(scope='session')
def browser(request):
	return request.config.getoption("--browser")


@fixture(scope='session')
def is_headless(request):
	return request.config.getoption("--is_headless")

