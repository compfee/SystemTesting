
from expected_results.page_content.base_page_content import BasePageContent


class LoginPageContent(BasePageContent):

	TITLE_ERROR = BasePageContent.TITLE + 'Error'

	URL = BasePageContent.URL + 'login.htm'

	ERROR_TITLE = 'Error!'
	NO_SUCH_USER_ERROR_MESSAGE = 'The username and password could not be verified.'
	EMPTY_FIELDS_ERROR_MESSAGE = 'Please enter a username and password.'



