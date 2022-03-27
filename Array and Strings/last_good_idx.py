# given an array find whether we reach the last index or not by jumping by index valuing or =< 1 of the index value.


# tranverse the array from last to begging and check whether we reach the the next index by the current value of not.

def jumping_to_last(arr):
	lastGoodIndex = arr[-1]
	for i in range(len(arr)-1, -1, -1):
		if arr[i] + i >= arr[i]:
			lastGoodIndex = i
	
	return lastGoodIndex == 0


def main():
	arr = [3,1,1,4,1,7]
	print(jumping_to_last(arr))


if __name__ == '__main__':
	main()
