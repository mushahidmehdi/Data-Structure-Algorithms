

# Given an integer array nums, find the maximum value of j-i such that nums[j] > nums[i].


def maximun_difference(arr):
	auxilary_array = [0] * len(arr)
	auxilary_array[len(arr) -1] = arr[len(arr) -1]
	print('auxilary array:', auxilary_array)

	for i in range(len(arr) -1, -1, -1):
		print(i)


array = [9, 10, 2, 6, 7, 12, 8, 1]
print('The maximum value is', maximun_difference(array))
