
import time


def refresh_page(expected, page, sleep_time=3):


	counter = 0
	while expected != page.title() and counter < 5:
		print("\nERROR: expected page title {} != {}.\nTrying to refresh...\n".format(expected, page.title()))
		page.driver.refresh()
		counter += 1
		time.sleep(sleep_time)

	if expected != page.title():
		raise Exception("\nERROR: This site can't be reached\n")

	return None
