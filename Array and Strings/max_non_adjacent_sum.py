# Given an arry return the maximun non consective sum of the array.
# [4,2,3,5,1,6,7] -> 16
# [4,4,7,7,8,13,15]


def max_non_consective_sum(arr:list):

	if len(arr) == 0:
		return 'Empty Arr'

	if len(arr) == 1:
		return arr[0]

	max_arr = [0 for i in range(len(arr))]
	max_arr[0] = arr[0]
	max_arr[1] = arr[0] if arr[0] > arr[1] else arr[1]

	for i in range(2, len(arr)):
		max_arr[i] = max(max_arr[i-2] + arr[i], max_arr[i-1])
	
	return max_arr

	
def main():
	array = [4,2,3,5,1,6,7]
	print(max_non_consective_sum(array))

if __name__ == '__main__':
	main()