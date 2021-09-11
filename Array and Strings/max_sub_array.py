# By using two for loops cur and runner we can find the max sub arr with runtime of O(n**2)
# Kadane's algorithm find the maximum sum of a contiguous subarray in an array with a runtime of O(n).

def max_sub_arr(arr):
	best_max = arr[0]
	curr_max = 0
	for i in range(len(arr)):
		curr_max = curr_max + arr[i]
		if curr_max < 0:
			curr_max = 0
		if curr_max > best_max:
			best_max = curr_max
	return best_max
 

def main():
	arr = [2, 5, 7, 7, -10, 3, 4, 10]
	arr = [-1, 6, 7, -2, 0, 3,-4 ,-4]
	print(max_sub_arr(arr))

if __name__ == '__main__':
	main()

# https://favtutor.com/blogs/kadanes-algorithm-python