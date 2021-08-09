import unittest
from unittest import result
from unittest.case import TestCase

def urlify_pythonic(str, len):
	return str[:len].replace(' ', '%20')


def urlify(str, len):
	result = ''
	new_str = str[:len]
	for i in new_str:
		if i == ' ':
			result += "%20"
		else:
			result += i 
		
	return result




class Test(unittest.TestCase):
	def test_urlify(self):
		self.assertEqual(urlify('much ado about nothing      ', 22), "much%20ado%20about%20nothing")
		self.assertEqual(urlify("Mr John Smith       ", 13), "Mr%20John%20Smith")
		self.assertEqual(urlify(" a b", 4), "%20a%20b")

	def test_urlify_pythonic(self):
		self.assertEqual(urlify_pythonic('much ado about nothing      ', 22), "much%20ado%20about%20nothing")
		self.assertEqual(urlify_pythonic("Mr John Smith       ", 13), "Mr%20John%20Smith")
		self.assertEqual(urlify_pythonic(" a b", 4), "%20a%20b")


if __name__ == '__main__':
	unittest.main()