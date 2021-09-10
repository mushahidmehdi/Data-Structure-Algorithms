# Binary search is divide and conquer algorithem to search an element in a sorted arr.

def find_x(arr, ele):
	# check if the elemnt is within the range of array.
	if ele < arr[0] or ele > arr[-1]:
		return False
	lenArr = len(arr)
	mid = lenArr//2
	if ele == arr[mid]:
		return True
	if ele < arr[mid]:
		return find_x(arr[:mid], ele)
	else:
		return find_x(arr[mid:], ele)

def main():
	arr = [ 2, 3, 4, 10, 40 ]
	x = 400
	print(find_x(arr, x))


if __name__ == '__main__':
	main()