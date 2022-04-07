
import requests


def get_http_status_code(url):

	try:
		r = requests.get(url)
		print("\nURL: {}\nHTTP Status code: {}".format(url, r.status_code))
	except ConnectionError as er:
		print('\n{}\n'.format(er))
	return None
