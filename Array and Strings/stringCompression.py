# String Compressor
# example, the string ‘aabcccccaaa’ would become a2b1c5a3.
import unittest

def compressed_string(string):
	prevChar = ''
	compSent = ''
	counter = 0
	for i in string:
		if i == prevChar:
			counter += 1
		else:
			if counter != 0:
				compSent += prevChar + str(counter)
			prevChar = i
			counter = 1
	compSent += prevChar + str(counter)

	if len(compSent) < len(string):
		return compSent
	else:
		return string

class Test(unittest.TestCase):
	def test_compressed(self):
		self.assertEqual(compressed_string("aabcccccaaa"), "a2b1c5a3")
		self.assertEqual(compressed_string("abcdef"), "abcdef")
		self.assertEqual(compressed_string("aaa"), "a3")
		self.assertEqual(compressed_string("a"), "a")
		self.assertEqual(compressed_string(""), "")
		self.assertNotEqual(compressed_string("aabb"), "a1b1")

if __name__ == '__main__':
	unittest.main()