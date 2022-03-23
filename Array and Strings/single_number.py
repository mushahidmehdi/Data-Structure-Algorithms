# Given an array remove all number whwich has occer twice

def remove_duplicates(arr):

	result = 0
	for i in range(len(arr)):
		result ^= arr[i]
	
	return result

def main():
	arr = [3,5,6,9,3,5,6,9,7,45,7]
	print(remove_duplicates(arr))

if __name__ == '__main__':
	main()