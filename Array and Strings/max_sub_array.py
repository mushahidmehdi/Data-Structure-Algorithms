# By using two for loops cur and runner we can find the max sub arr with runtime of O(n**2)
# Kadane's algorithm find the maximum sum of a contiguous subarray in an array with a runtime of O(n).

def max_sum_sub_arr(arr, len):
	maxArr = 0
	currMax = 0
	for i in range(len):
		currMax += arr[i]
		if currMax < 0:
			currMax = 0
		if currMax > maxArr:
			maxArr = currMax
	return maxArr


def main():
	arr = [2, 5, 7, 7, -10, 3, 4, -10]
	#arr = [-1, 6, 7, -2, 0, 3,-4 ,-4]
	print('Kadane\'s max sub array:', end='')
	print(max_sum_sub_arr(arr, len(arr)))

if __name__ == '__main__':
	main()

# https://favtutor.com/blogs/kadanes-algorithm-python