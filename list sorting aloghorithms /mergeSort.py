numList = [2, 3, 4, 5, 12, 1, 2, 0, 89, 344, 3434, 3, 6, 7, 90, 99, 11]
	
def merge(left, right):
	sorted_arr = []
	i, j = 0, 0
	while len(left) > i and len(right) > j:
		if left[i] < right[j]:
			sorted_arr.append(left[i])
			i += 1
		else:
			sorted_arr.append(right[j])
			j += 1
	while len(left) > i:
		sorted_arr.append(left[i])
		i += 1
	while len(right) > j:
		sorted_arr.append(right[j])
		j += 1
	return sorted_arr


def merge_sort(arr):
	if len(arr) < 2:
		return arr
	half = len(arr)//2
	left = merge_sort(arr[:half]) 
	right = merge_sort(arr[half:])
	return merge(left, right)

print(merge_sort(numList))