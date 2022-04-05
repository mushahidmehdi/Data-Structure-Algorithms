
# given an unordered array with minimun swap change the order to ordered array.


def number_swap(arr:list) -> int:
	swaps = 0
	for i in range(len(arr)):
			index = arr[i] - 1
			if arr[index] != arr[i]:
				arr[index], arr[i]= arr[i], arr[index]
				swaps += 1
				
	for i in range(len(arr)):
			index = arr[i] - 1
			if arr[index] != arr[i]:
				arr[index], arr[i]= arr[i], arr[index]
				swaps += 1
	return swaps
	
	
def main():
	arr = [7,1,3,2,4,5,6]
	arr1 = [8,4,3,1,9,2,5,7,6]
	print(number_swap(arr1))

if __name__ == '__main__':
	main()

