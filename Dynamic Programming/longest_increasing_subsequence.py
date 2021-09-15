# Given a arr find the longest sequence sub array. Run time Quadratic:

def longest_sub_len(arr):
	long_subs = [1 for i in range(len(arr))]
	for i in range(1, len(arr)):
		for j in range(len(arr)):
			if arr[j] > arr[i] and long_subs[j] <= long_subs[i]:
				long_subs[j] = long_subs[i] + 1

	return max(long_subs)

def main():
	#arr = [2,4,6,8,9,2,12,1,17]
	arr = [2,24,6,18,9,2,12,1,17]
	#arr = [-2,4,6,-8,9,2,-12,1,17]
	print(longest_sub_len(arr))

if __name__ == '__main__':
	main()
