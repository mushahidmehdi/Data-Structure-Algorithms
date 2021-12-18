# The Levenshtein distance 
# kitten —> sitten (substitution of s for k)
# sitten —> sittin (substitution of i for e)
# sittin —> sitting (insertion of g at the end)
# check whether is there a single distance bewteen the two strings


import unittest

def lavinstian_dist(str1, str2):
	if abs(len(str1) - len(str2)) > 1:
		return False

	diff = 0
	i = j = 0

	while i < len(str1) and j < len(str2):
		if str1[i] != str2[j]:
			if len(str1) > len(str2):
				j += 1
				diff += 1
			elif len(str1) < len(str2):
				i += 1
				diff += 1

			else:
				i += 1 
				j += 1
				diff += 1
		else:	
			i += 1 
			j += 1

 	# checking for any empty string
	if i < len(str1):
		i += 1
		diff += 1

	if j < len(str2):
		j += 1
		diff += 1

	return diff == 1
		

		
class LavinstainDistance(unittest.TestCase):
	def test_lavinstain_dist(self):
		self.assertTrue(lavinstian_dist('a', ''), True)
		self.assertFalse(lavinstian_dist('abc', 'abde'), False)
		self.assertFalse(lavinstian_dist('', 'abd'), False)
		self.assertFalse(lavinstian_dist('ddd', 'abd'), False)
		self.assertFalse(lavinstian_dist('abcsdfsdf', 'abd'), False)
		self.assertFalse(lavinstian_dist('abc', ''), False)
		self.assertFalse(lavinstian_dist('abc', 'abcdabcd'), False)
		self.assertTrue(lavinstian_dist('abc', 'abd'), True)
		self.assertTrue(lavinstian_dist('a', ''), True)
		self.assertTrue(lavinstian_dist('', 'd'), True)
		self.assertTrue(lavinstian_dist('abc', 'abi'), True)
		self.assertTrue(lavinstian_dist('abi', 'abd'), True)



if __name__ == '__main__':
	unittest.main()