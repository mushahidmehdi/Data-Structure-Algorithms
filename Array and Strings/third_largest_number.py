# given an array find the third largest number.
import sys

def third_largest_number(arr:list) -> int:
	if len(arr) < 3:
		return 'Arry len is less than 3'

	first = -sys.maxsize
	second = -sys.maxsize
	third = -sys.maxsize

	for num in range(len(arr)):

		if arr[num] > first:
			third = second
			second = first
			first = arr[num]

		elif arr[num] > second:
			third = second
			second = arr[num]
		
		elif arr[num] > third:
			third = arr[num]
	
	return third


def main():
	arr = [3,6,8,5,7,2,9,88,99,101]
	print(third_largest_number(arr))
if __name__ == '__main__':
	print(float('-inf'))
	main()