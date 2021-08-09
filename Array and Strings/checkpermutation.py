# Checking permutation.

import unittest
from collections import Counter

def checking_permutation_pythonic(str1, str2):
	if len(str1) != len(str2):
		return False

	return Counter(str1) == Counter(str2)
	

def checking_permutation(str1, str2):
	counter1 = {}
	for i in str1:
		counter1[i] = counter1.get(i, 0) + 1
	counter2 = {}
	for i in str2:
		counter2[i] = counter2.get(i, 0) + 1
	if counter2 != counter1:
		return False
	return True
	

class Test(unittest.TestCase):
	def test_permutation_pythonic(self):
		self.assertTrue(checking_permutation_pythonic('abc', 'bac'), True)
		self.assertFalse(checking_permutation_pythonic('abcee', 'bac'), False)
		self.assertTrue(checking_permutation_pythonic('aEbEc', 'bacEE'), True)
		self.assertFalse(checking_permutation_pythonic('abcTY', 'bac'), False)

	def test_permutation(self):
		self.assertTrue(checking_permutation('abc', 'bac'), True)
		self.assertFalse(checking_permutation('abcee', 'bac'), False)
		self.assertTrue(checking_permutation('aEbEc', 'bacEE'), True)
		self.assertFalse(checking_permutation('abcTY', 'bac'), False)




if __name__ == '__main__':
	unittest.main()