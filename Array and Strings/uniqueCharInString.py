# given a string determine whether each element in the string is unique or not;

import unittest

def is_unique_using_set(string):
	return len(string) == len(set(string))

def is_unique_using_dict(string):
	char_counter = {}
	for i in string:
		if i in char_counter:
			return False
		char_counter[i] = 1
	return True


class Test(unittest.TestCase):
	def test_is_unique_using_set(self):
		self.assertTrue(is_unique_using_set('abcd'), True)
		self.assertTrue(is_unique_using_set('xyz'), True)
		self.assertFalse(is_unique_using_set('aabc'), False)
		self.assertTrue(is_unique_using_set('abcrde'), True)
		self.assertFalse(is_unique_using_set('*9b()aa14'), False)
		self.assertTrue(is_unique_using_set("".join([chr(val) for val in range(128)])), True)

	
	def test_is_unique_using_dict(self):
		self.assertTrue(is_unique_using_dict('abcd'), True)
		self.assertTrue(is_unique_using_dict('xyz'), True)
		self.assertFalse(is_unique_using_dict('aabc'), False)
		self.assertTrue(is_unique_using_dict('abcrde'), True)
		self.assertFalse(is_unique_using_dict('*9ba144'), False)
		self.assertTrue(is_unique_using_dict("".join([chr(val) for val in range(128)])), True)
		
		
if __name__ == '__main__':
	unittest.main()