# By using two for loops cur and runner we can find the max sub arr with runtime of O(n**2)

# Kadane's algorithm find the maximum sum of a contiguous subarray in an array with a runtime of O(n).


# https://favtutor.com/blogs/kadanes-algorithm-python



def max_continous_sum(arr):
	current_max = 0
	max_sum = 0

	for i in range(len(arr)):
		current_max += arr[i]

		if current_max < 0:
			current_max = 0

		if current_max > max_sum:
			max_sum = current_max

	return max_sum


def main():
	arr = [1,4,5,6,-2,-6,-9,0,1,2]
	arr = [-1, 6, 7, -2, 0, 3,-4 ,-4]
	print('the maximum sub array is: ', end='')
	print(max_continous_sum(arr))

if __name__ == '__main__':
	main()