import unittest

def rotate_matrix(matrix):
	lenght = len(matrix)
	new_matrix = [[0]*lenght for i in range(lenght)]
	for i, j in zip(range(lenght), range(lenght-1, -1, -1)):
		for k in range(lenght):
			new_matrix[k][i] = matrix[j][k]
	return new_matrix

class Test(unittest.TestCase):
	def test_rotate(self):
		self.assertEqual(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
		[[7, 4, 1], [8, 5, 2], [9, 6, 3]])
		self.assertEqual(rotate_matrix([[1, 2, 3, 4, 5],
		[6, 7, 8, 9, 10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20],
		[21, 22, 23, 24, 25]]),
		[[21, 16, 11, 6, 1],
		[22, 17, 12, 7, 2],
		[23, 18, 13, 8, 3],
		[24, 19, 14, 9, 4],
		[25, 20, 15, 10, 5]])

if __name__ == '__main__':
	unittest.main()