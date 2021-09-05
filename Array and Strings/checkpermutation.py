# Checking for permutation: different order in which the element of sequence can be arrange.
# Two permuted dict will always equal to each other.

import unittest
from collections import Counter, defaultdict

def checking_permutation_pythonic(str1, str2):
	if len(str1) != len(str2):
		return False

	# Counter is a subclass of dict that's specially designed for counting hashable objects in Python.
	return Counter(str1) == Counter(str2)
	

def checking_permutation(str1, str2):
	if len(str1) != len(str2):
		return False
	counter1 = {}
	for i in str1:
		# https://docs.python.org/3/library/stdtypes.html#dict.get
		# i is key with default value None, we used 0
		counter1[i] = counter1.get(i, 0) + 1
	counter2 = {}
	for i in str2:
		counter2[i] = counter2.get(i, 0) + 1
	if counter2 != counter1:
		return False
	return True
	

def using_defaultdict(str1, str2):
	if len(str1) != len(str2):
		return False
	counter1 = defaultdict(int)
	counter2 = defaultdict(int)
	for str in str1:
		counter1[str] = counter1.get(str, 0) + 1
	for str in str2:
		counter2[str] = counter2.get(str, 0) + 1
	
	if counter1 == counter2:
		return True
	else:
		return False



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

	def test_defaultdict(self):
		self.assertTrue(using_defaultdict('abc', 'bac'), True)
		self.assertFalse(using_defaultdict('abcee', 'bac'), False)
		self.assertTrue(using_defaultdict('aEbEc', 'bacEE'), True)
		self.assertFalse(using_defaultdict('abcTY', 'bac'), False)





if __name__ == '__main__':
	unittest.main()