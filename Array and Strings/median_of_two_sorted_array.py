# Median of two sorted arrays of different sizes

def median_two_sorted_arr(arr1: list, arr2:list) -> int:

	i = j = k = 0
	new_arr = []
	while len(arr1) > i and len(arr2) > j:
		if arr1[i] < arr2[j]:
			new_arr.append(arr1[i])
			i += 1
		else:
			new_arr.append(arr2[j])
			j += 1
		k += 1
	
	while len(arr1)>i:
		new_arr.append(arr1[i])
		i += 1

	while len(arr2)>j:
		new_arr.append(arr2[j])
		j += 1


	n = len(new_arr)
	mid = n//2
	if n % 2 == 0:
		return (new_arr[mid] + new_arr[mid-1])/2

	return new_arr[mid]


def main():
	array1 = [2,4,6,8,10]
	array2 = [1,3,5,7,9,11]
	print(median_two_sorted_arr(array1, array2))

if __name__ == '__main__':
	main()