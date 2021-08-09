# Check whether the given string is palindrome or not.

from logging import StringTemplateStyle
import unittest

def palindrome_pythonic(str):
	str = str.replace(' ', '')
	new_str = "".join(reversed(str))
	if str == new_str:
		return str
	

def palindrome(str):
	str = str.replace(' ', '')
	if str == str[::-1]:
		return str
class Test(unittest.TestCase):
	def test_palindrome_pythonic(self):
		self.assertEqual(palindrome_pythonic('aba'), 'aba')
		self.assertEqual(palindrome_pythonic('redivider'), 'redivider')
		self.assertEqual(palindrome_pythonic('mr owl ate my metal worm'), 'mrowlatemymetalworm' )
	def test_palindrome(self):
		self.assertEqual(palindrome('aba'), 'aba')
		self.assertEqual(palindrome('redivider'), 'redivider')
		self.assertEqual(palindrome('mr owl ate my metal worm'), 'mrowlatemymetalworm')


if __name__ == '__main__':
	unittest.main()