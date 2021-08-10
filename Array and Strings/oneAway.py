# The Levenshtein distance 
# kitten —> sitten (substitution of s for k)
# sitten —> sittin (substitution of i for e)
# sittin —> sitting (insertion of g at the end)
# check whether there is a single distance bewteen the two strings.

import unittest

def one_away(s1, s2):
	lenS1 = len(s1)
	lenS2 = len(s2)

	# if the diffence is greater than one return False
	if abs(lenS1 - lenS2) > 1:
		return False

	edits = 0
	i = j = 0
	while i < lenS1 and j < lenS2:
		if s1[i] != s2[j]:
			if lenS1 > lenS2:
				i += 1
			elif lenS1 < lenS2:
				j += 1
			else:
				i += 1
				j += 1
			edits += 1
		else:
			i += 1
			j += 1
	if i < lenS1:
		edits += 1
	if j < lenS2:
		edits += 1
	return edits == 1

 
class Test(unittest.TestCase):
	def test_one_away(self):
		self.assertTrue(one_away("xyz", "xz"), True)
		self.assertTrue(one_away("xyz", "xyyz"), True)
		self.assertTrue(one_away("xyz", "xyx"), True)
		self.assertFalse(one_away("xyz", "xxx"), False)
		self.assertFalse(one_away("xyz", "xxx"), False)
		self.assertFalse(one_away("xyz", "xxx"), False)
		self.assertFalse(one_away("xyz", ""), False)
		self.assertTrue(one_away("x", ""), True)
		self.assertTrue(one_away("", "s"), True)


if __name__ == '__main__':
	unittest.main()
