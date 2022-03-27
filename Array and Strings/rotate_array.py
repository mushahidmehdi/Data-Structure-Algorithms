# given an array rotate the array by k, where k is a positive integer, to the right.

# Example:
# [2,5,6,7,9,11,57] rotate by 3 ---> [7,9,11,57,2,5,6]


def rotate_right(arr: list, num: int) -> list:
	
	arr.reverse()
	first_arr = list(reversed(arr[:len(arr)-num]))
	last_arr = list(reversed(arr[len(arr)-num:]))
	return first_arr + last_arr
	
	


def main():
	arr = [2,5,6,7,9,11,57]
	print(rotate_right(arr, 3))

if __name__ == '__main__':
	main()