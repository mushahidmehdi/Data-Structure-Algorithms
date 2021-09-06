# in the given matrix if any of the element is zero change all the elemet in its column and row into 0:
# method:
# fing the colums and rows where the the values are zeros add it into a set.
# loop over again over the matrix and if any of the value found in rows or cols them then make the entire row and col changed into 0.

import unittest

def zero_matrix(mtx):
	len_dim = len(mtx)
	rows = set()
	cols = set()
	for row in range(len_dim):
		for col in range(len_dim):
			if mtx[row][col] == 0:
				rows.add(row)
				cols.add(col)

	for r in range(len_dim):
		for c in range(len_dim):
			if (r in rows) or (c in cols):
				mtx[r][c] = 0

	return mtx
	

class Test(unittest.TestCase):

	test_case = [
		(
			[[1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
			[11, 12, 13, 14, 15],
			[16, 0, 18, 19, 20],
			[21, 22, 23, 24, 25]],

			[[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[11, 0, 13, 14, 0],
			[0, 0, 0, 0, 0],
			[21, 0, 23, 24, 0]],
		),
		(
			[[3, 4, 0],
            [ 8, 9,10],
			[ 13, 14, 15]],

			[[0, 0, 0],
			[ 8, 9, 0],
			[13, 14, 0]
			],
		),
		(
			[[1, 2, 3, 4],
            [6, 0, 8, 9],
			[11, 12, 13, 14],
			[16, 0, 18, 19],
			],

			[[1, 0, 3, 4],
			[0, 0, 0, 0],
			[11, 0, 13, 14],
			[0, 0, 0, 0]
			],
		),
		]

	test_func = [zero_matrix]

	def test_zero_mtx(self):
		for fun in self.test_func:
			for [test_mtx, res_mtx] in self.test_case:
				self.assertEqual(fun(test_mtx), res_mtx)

if __name__ == '__main__':
	unittest.main()


