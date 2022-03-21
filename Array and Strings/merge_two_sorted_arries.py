# given two arries merge them into a single array.

def merge_two_arries(arr_1: list, arr_2:list) -> list:
	arr_3 = []
	i = j = 0

	while i < len(arr_1) and j < len(arr_2):
		if arr_1[i] < arr_2[j]:
			arr_3.append(arr_1[i])
			i += 1
		else: 
			arr_3.append(arr_2[j])
			j += 1
		
	if i < len(arr_1):
		arr_3.append(arr_1[i])
		i += 1
	if j < len(arr_2):
		arr_3.append(arr_2[j])
		j += 1
	
	return arr_3

def main():
	array1 = [2, 9, 22, 43, 66, 98, 202, 5000]
	array2 = [1, 2, 24, 44, 64, 99, 301, 400]
	ans = merge_two_arries(array1, array2)
	print(ans)


if __name__ == '__main__':
	main()


		