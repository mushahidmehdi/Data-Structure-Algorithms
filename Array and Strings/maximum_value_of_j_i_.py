
# Given an integer array, find the max value of j-i such that nums[j] > nums[i].

# https://www.techiedelight.com/find-maximum-value-index-array/

def maximun_difference(arr):
	auxilary_array = [0] * len(arr)
	auxilary_array[len(arr) -1] = arr[len(arr) -1]

	for i in range(len(arr)-2, -1, -1):
		auxilary_array[i] = max(arr[i], auxilary_array[i+1])
	
	i = j = 0
	diff = float('-inf')
	while i < len(arr) and j < len(auxilary_array):
		if arr[i] < auxilary_array[j]:
			diff = max(diff, j-i)
			j += 1
		else:
			i += 1
	return diff


def main():
	array = [9, 10, 2, 6, 7, 12, 8, 1]
	print('The maximum value is', maximun_difference(array))

if __name__ == '__main__':
	main()
