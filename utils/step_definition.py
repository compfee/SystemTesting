
import collections
import allure


def step_definition(self, step_description, expected, actual, act=None, click=False):

	with allure.step(step_description):

		# Arrange
		expected = expected

		# Act
		# check if a function just a click (no parameters required)
		if act:
			if not click:
				act(expected)
			else:
				act()

		# Assert
		# check if an object is a function
		if isinstance(actual, collections.Callable):
			actual_result = actual()
		else:
			actual_result = actual

		# Log
		print('\nStep: {}\nExpected: {}\nActual: {}'.format(step_description,
		                                                    expected,
		                                                    actual_result))
		self.assertEqual(expected,
		                 actual_result,
		                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
		                                                                                    actual_result))

		return None
