
## Given an array return all the duplicate elements in linear runtime and O(1) space complexity.
# Note all the elements are within 1 to len(arr). 


def return_duplicates(arr: list)-> list:

	new_arr = []
	for i in range(len(arr)):
		index = abs(arr[i]) - 1
		if arr[index] < 0:
			new_arr.append(index+1)
		arr[index] = -arr[index]

	return new_arr

def main():
	arr = [1,1,4,5,6,2,4]
	print(return_duplicates(arr))


if __name__ == '__main__':
	main()