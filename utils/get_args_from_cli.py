
import sys


def get_args():


	is_headless, browser, env = None, None, None

	for param in sys.argv:

		if '--env=' in param:
			env = str(param).replace('--env=', '')
			# print("\nParam: {}".format(env))

		if '--browser=' in param:
			browser = str(param).replace('--browser=', '')
			# print("\nParam: {}".format(browser))

		if '--is_headless=' in param:
			is_headless = True if str(param).replace('--is_headless=', '') == 'True' else False
			# print("\nParam: {}".format(is_headless))

	if env is None:
		raise Exception("Please add '--env=<data>' argument to the command line")

	if browser is None:
		raise Exception("Please add '--browser=<data>' argument to the command line")

	if is_headless is None:
		raise Exception("Please add '--is_headless=<data>' argument to the command line")

	return {'env': env, 'browser': browser, 'is_headless': is_headless}
