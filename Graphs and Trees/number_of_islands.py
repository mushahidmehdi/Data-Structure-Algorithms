# Given a set of 0s and "1"s; find number of "1"'s as seprated entitiy the 1's that are connected by rows or columns will be consider as single entity.

# To solve this problem: we will used depth first search, if there is 1 in the matrix we will check for top, bottom, left and right the one if there any neighbors is one we will recursively run the dfs again util all the neighbor in top, bottom, left and right are visitited and during each itteration we will changed the value of 1 to 0.

def dfs(r, c, grid):
	"""utility func to check in for 1s in rows and columns"""
	grid[r][c] = "0"
	neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
	for row, col in neighbors:
		if row >= 0 and col >= 0 and len(grid) > row and len(grid[row]) > col and grid[row][col] == "1":
			dfs(row, col, grid)

def finding_ones(grid):
	entities = 0
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == "1":
				dfs(r, c, grid)
				entities += 1
	return entities

if __name__ == '__main__':
	grid = [["1","1","0","0","0"],
			["1","1","1","1","0"],
			["0","0","0","1","0"],
			["0","0","0","0","1"]]
	print(finding_ones(grid))


