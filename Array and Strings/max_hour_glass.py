
# Given an two d arr find the the sum of the given pattern and return the maximin sum.

# 2, 3, 5
#    4           ----> 21
# 1, 2, 4 


def get_max_in_arr(matrix, row, col):
	sum = 0
	sum += matrix[row-1][col-1]
	sum += matrix[row-1][col]
	sum += matrix[row-1][col+1]
	sum += matrix[row][col]
	sum += matrix[row+1][col-1]
	sum += matrix[row+1][col]
	sum += matrix[row+1][col+1]
	return sum


arr = []
for i in range(6):
	arr_temp = [int(inp) for inp in input().strip().split(' ')]
	arr.append(arr_temp)

maxi = float('-inf')

for row in range(1, len(arr)-1):
	for col in range(1, len(arr[row])-1):
		curr_max = get_max_in_arr(arr, row, col)
		maxi = max(maxi, curr_max)
	
print(maxi)
