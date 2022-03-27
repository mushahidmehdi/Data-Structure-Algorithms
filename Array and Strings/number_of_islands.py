# given a two dimentional array with 1s and 0s where 1 represent an island and 0 as water find all the islands in the matrix all the adjacent 1s will consider a single island.


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


def main():
	islands = [
	['1', '1', '1', '1', '0', '1'],
	['1', '1', '0', '0', '0', '0'],
	['1', '0', '1', '0', '1', '1'],
	['0', '0', '0', '1', '1', '0']
	]
	print(number_islands(islands))

if __name__ == '__main__':
	main()
