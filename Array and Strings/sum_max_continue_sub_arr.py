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


# if the arry is circular, we will track both maximin positive and maximin negative as well as the array sum and return the maximm of either maximin positive or difference of array sum and maximun negative


def max_continous_circular_arr(arr):
	curr_max = curr_min = total_max = 0
	pos_max = float('-inf')
	min_max = float('inf')

	for i in range(len(arr)):
		total_max += arr[i]

		curr_max += arr[i]

		if curr_max > pos_max:
			pos_max = curr_max

		if curr_max < 0:
			curr_max = 0
		
		curr_min += arr[i] 
		if curr_min < min_max:
			min_max = curr_min
		
		if curr_min > 0:
			curr_min = 0
	
	print('Total max',total_max)
	print('Minimun max',min_max)
	print('positive max', pos_max)
		
	if total_max == min_max:
		return pos_max

	return max(pos_max, (total_max - min_max))

	


def main():
	arr = [1, 4, 5, 6, -2, -6, -9, 0, 1, 2]
	arr2 = [-1, -3, -2, 6, -1 ,4]
	# print('the maximum sub array is: ', end='')
	# print(max_continous_sum(arr))
	# print("max Continous Sum: ", end='')
	print(max_continous_circular_arr(arr2))
if __name__ == '__main__':
	main()