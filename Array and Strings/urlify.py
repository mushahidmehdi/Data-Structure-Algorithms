import unittest
from unittest.case import TestCase

def urlify_pythonic(str, len):
	return str[:len].replace(' ', '%20')


class Test(unittest.TestCase):
	def test_urlify(self):
		self.assertEqual(urlify_pythonic('much ado about nothing      ', 22), "much%20ado%20about%20nothing")
		self.assertEqual(urlify_pythonic("Mr John Smith       ", 13), "Mr%20John%20Smith")
		self.assertEqual(urlify_pythonic(" a b", 4), "%20a%20b")


if __name__ == '__main__':
	unittest.main()