# Check whether the given string is palindrome or not.
# palindrome means both from beggening to and end and to end to start of a string is same;
import unittest

def sliceing_palindrome(strg):
	# removing space from string
	strg = strg.replace(' ', '')
	# removing puncutation
	punctations = '!@#$%^&*()+_}|{":?<>,./'
	for pun in punctations:
		strg = strg.replace(pun, '')
	# lowering all the cases:
	strg = strg.lower()

	if strg == strg[::-1]:
		return True
	return False
	
def reversing_palindrome(strg):
	# removing space from string
	strg = strg.replace(' ', '')
	# removing puncutation
	punctations = '!@#$%^&*()+_}|{":?<>.,/'
	for pun in punctations:
		strg = strg.replace(pun, '')
	# lowering all the cases:
	strg = strg.lower()

	# first reverse the string which gives us the memory location then join the string by empty space
	if strg == ''.join(reversed(strg)):
		return True
	return False


class Palindrome(unittest.TestCase):
	def test_slice_pal(self):
		self.assertTrue(sliceing_palindrome('Mr owl ate my metal worm?'))
		self.assertTrue(sliceing_palindrome('redivider'))
		self.assertTrue(sliceing_palindrome('aba'))
		self.assertTrue(sliceing_palindrome('Aba'))
		self.assertTrue(sliceing_palindrome(' Aba '))
		self.assertFalse(sliceing_palindrome('abcdefgh'))
	def test_reverse_pal(self):
		self.assertTrue(reversing_palindrome('Mr owl ate my metal worm.'))
		self.assertTrue(reversing_palindrome('redivider'))
		self.assertTrue(reversing_palindrome('aba'))
		self.assertFalse(reversing_palindrome('abcdefg'))

if __name__ == '__main__':
	unittest.main()