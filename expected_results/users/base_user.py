
class BaseUser:

	def __init__(self, user_template):
		self._first_name = user_template.FIRST_NAME
		self._last_name = user_template.LAST_NAME

		self._address = user_template.ADDRESS
		self._city = user_template.CITY
		self._state = user_template.STATE
		self._zip_code = user_template.ZIP_CODE
		self._phone = user_template.PHONE

		self._username = user_template.USERNAME
		self._password = user_template.PASSWORD

		self._ssn = user_template.SSN

		self._init_balance = user_template.INIT_BALANCE
		self._balance = user_template.INIT_BALANCE
		self._min_balance = user_template.MIN_BALANCE

		self._email = "{}_{}@mail.com".format(self.first_name, self.last_name)

		self._print_user_data()

	def _print_user_data(self):

		print('First Name: {}\n'
		      'Last Name: {}\n'
		      'Address: {}\n'
		      'City: {}\n'
		      'State: {}\n'
		      'Zip Code: {}\n'
		      'Phone #: {}\n'
		      'SSN: {}\n'
		      'Username: {}\n'
		      'Password: {}\n'
		      'Email: {}\n'.format(self.first_name,
		                           self.last_name,
		                           self.address,
		                           self.city,
		                           self.state,
		                           self.zip_code,
		                           self.phone,
		                           self.ssn,
		                           self.username,
		                           self.password,
		                           self.email))

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, name: str):
		self._first_name = name

	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, name: str):
		self._last_name = name

	@property
	def address(self):
		return self._address

	@address.setter
	def address(self, address: str):
		self._address = address

	@property
	def city(self):
		return self._city

	@city.setter
	def city(self, city: str):
		self._city = city

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, state: str):
		self._state = state

	@property
	def zip_code(self):
		return self._zip_code

	@zip_code.setter
	def zip_code(self, zip_code: str):
		self._zip_code = zip_code

	@property
	def phone(self):
		return self._phone

	@phone.setter
	def phone(self, phone: str):
		self._phone = phone

	@property
	def ssn(self):
		return self._ssn

	@ssn.setter
	def ssn(self, ssn: str):
		self._ssn = ssn

	@property
	def username(self):
		return self._username

	@username.setter
	def username(self, username: str):
		self._username = username

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, password: str):
		self._password = password

	@property
	def email(self):
		return self._password

	@email.setter
	def email(self, email: str):
		self._email = email

	@property
	def balance(self):
		return self._balance

	@balance.setter
	def balance(self, new_balance):
		self._balance = new_balance

