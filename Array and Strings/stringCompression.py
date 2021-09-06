# String Compressor
# example, the string ‘aabcccccaaa’ would become a2b1c5a3.
import unittest

def compress_string_by_count_itter(string):
	counter = 0; prev_ele = ''; compressed_string = ''
	for i in string:
		if prev_ele == i:
			counter += 1
		else:
			if counter != 0:
				compressed_string += prev_ele + str(counter)
			prev_ele = i
			counter = 1
	last_itter = prev_ele + str(counter)
	compressed_string = compressed_string + last_itter

	if len(compressed_string) < len(string):
		return compressed_string
	else:
		return string



class Test(unittest.TestCase):
    def test_compressed(self):
        self.assertEqual(compress_string_by_count_itter("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_string_by_count_itter("abcdef"), "abcdef")
        self.assertEqual(compress_string_by_count_itter("aaa"), "a3")
        self.assertEqual(compress_string_by_count_itter("a"), "a")
        self.assertEqual(compress_string_by_count_itter(""), "")
        self.assertNotEqual(compress_string_by_count_itter("aabb"), "a1b1")


if __name__ == '__main__':
    unittest.main()
