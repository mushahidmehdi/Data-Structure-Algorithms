# Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# optimal solution would be binary search: O(nlog(n))

def magic_index(arr):
	if len(arr) == 0:
		return False
	mid = len(arr)//2
	if mid == arr[mid]:
		return True
	elif mid < arr[mid]:
		return magic_index(arr[:mid])
	else:
		return magic_index(arr[mid:])


def main():
	arr =[-100,-50,-20,0,4,10,16]
	print(magic_index(arr))

if __name__ == '__main__':
	main()