# Given a set of 0s and "1"s; find number of "1"'s as seprated entitiy the 1's that are connected by rows or columns will be consider as single entity.

# To solve this problem: we will used depth first search, if there is 1 in the matrix we will check for top, bottom, left and right the one if there any neighbors is one we will recursively run the dfs again util all the neighbor in top, bottom, left and right are visited and during each itteration we will changed the value of 1 to 0.

import unittest

def dfs(matrix, row, col):
	matrix[row][col] = '0'
	check = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
	for r, c in check:
		if r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r]) and matrix[r][c] == '1':
			dfs(matrix, r, c)


def number_islands(matrix):
	islands = 0
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] == '1':
				islands += 1
				dfs(matrix, row, col)

	return islands


class NumberOfIslands(unittest.TestCase):
	def test_number_islands(self):
		self.assertEquals(number_islands(
				[['1','1','1','1','0','0'],
				['1','1','0','0','0','0'],
				['1','0','1','0','1','1'],
				['0','0','0','1','1','0']]), 3)
		self.assertEquals(number_islands(
				[["1","1","0","0","0"],
				["1","1","1","1","0"],
				["0","0","0","1","0"],
				["0","0","0","0","1"]]), 2)

	

if __name__ == '__main__':
	unittest.main()
