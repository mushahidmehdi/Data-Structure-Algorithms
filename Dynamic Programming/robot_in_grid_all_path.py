# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, Design an algorithm to find a path for the robot from the top left to the bottom right. 

# we will use dynamic programming to solved this problem, each time when we move a step away from the initial position we will add all the unique path into a new matrix by adding both top and left paths.
# The Asymtotic behaviour would be quadratic.

def find_path(rows, cols):
	# Check for the boundries: (base case)
	if rows == cols == 1:
		return 1
	matrix = [[1]*cols]*rows
	# we will start at matrix position 1,1
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
	return matrix[-1][-1]


def main():
	rows = 3
	cols = 2
	print(find_path(rows, cols))

if __name__ == '__main__':
	main()




















# video Explaination:
# https://www.youtube.com/watch?v=rBAxUTqvlQA

# Python Code:
# https://www.youtube.com/watch?v=gp_wfYhjALw