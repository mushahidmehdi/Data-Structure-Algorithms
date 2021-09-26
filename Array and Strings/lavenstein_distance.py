# The Levenshtein distance 
# kitten —> sitten (substitution of s for k)
# sitten —> sittin (substitution of i for e)
# sittin —> sitting (insertion of g at the end)
# check whether is there a single distance bewteen the two strings.

import unittest

def levenshtein_distance(str1, str2):
	len_str1= len(str1); len_str2 = len(str2)
	if abs(len_str1 - len_str2) > 1:
		return False
	dif = 0
	i = j = 0
	while len_str1 > i  and len_str2 > j:
		if str1[i] != str2[j]:
			if len_str1 > len_str1:
				i += 1
				dif += 1
			elif len_str1 < len_str2:
				j += 1
				dif += 1
			else:
				i += 1; j += 1
				dif += 1
		else:
			i += 1; j += 1
		
	# checking for any empty string
	if i < len_str1: dif += 1
	if j < len_str2: dif += 1
	
	return dif == 1


class Lavenstein(unittest.TestCase):
	def test_lavenstein_distance(self):
		self.assertFalse(levenshtein_distance('abc', 'abde'), False)
		self.assertFalse(levenshtein_distance('', 'abd'), False)
		self.assertFalse(levenshtein_distance('ddd', 'abd'), False)
		self.assertFalse(levenshtein_distance('abcsdfsdf', 'abd'), False)
		self.assertFalse(levenshtein_distance('abc', ''), False)
		self.assertFalse(levenshtein_distance('abc', 'abcdabcd'), False)
		self.assertTrue(levenshtein_distance('abc', 'abd'), True)
		self.assertTrue(levenshtein_distance('a', ''), True)
		self.assertTrue(levenshtein_distance('', 'd'), True)
		self.assertTrue(levenshtein_distance('abc', 'abi'), True)
		self.assertTrue(levenshtein_distance('abi', 'abd'), True)

if __name__ == '__main__':
	unittest.main()

				
		

