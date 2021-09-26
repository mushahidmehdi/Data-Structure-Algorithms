# write a function which urlify the sequence that mean if there is an empty space then add %20 init.
# remove space at the end of a the sequence before urlifying.

# remove any extra space at the end if sequence remove it by using rstrip method.
# in python used replace method to add %20 at the place of space.

import unittest

def urlify_pythonic(str):
	str = str.rstrip()
	return str.replace(' ', '%20')


def urlify(str):
	result = ''
	str = str.rstrip()
	for i in str:
		if i == ' ':
			result += "%20"
		else:
			result += i 
		
	return result



class Test(unittest.TestCase):
	def test_urlify(self):
		self.assertEqual(urlify('much ado about nothing      '), "much%20ado%20about%20nothing")
		self.assertEqual(urlify("Mr John Smith       "), "Mr%20John%20Smith")
		self.assertEqual(urlify(" a b"), "%20a%20b")

	def test_urlify_pythonic(self):
		self.assertEqual(urlify_pythonic('much ado about nothing      '), "much%20ado%20about%20nothing")
		self.assertEqual(urlify_pythonic("Mr John Smith       "), "Mr%20John%20Smith")
		self.assertEqual(urlify_pythonic(" a b"), "%20a%20b")


if __name__ == '__main__':
	unittest.main()