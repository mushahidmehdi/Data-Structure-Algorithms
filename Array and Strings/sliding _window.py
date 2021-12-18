# this problem is same as the max_sub_arr in same directory where it has been explain using kadan algorithm only differce is here the length of sub arr has been given.
# https://www.youtube.com/watch?v=__guhvzO540
# asymtotic function = len of arr * len of win (m*n)


def brute_force(arr, win=4):
	max_sum = 0
	for i in range(len(arr) - win + 1):
		win_sum = 0
		for j in range(win):
			win_sum += arr[i:][j]
			if win_sum > max_sum:
				max_sum = win_sum
	return max_sum


def sliding_window(nums: list, k: int) -> float:
	max_sum = 0
	_sum, start = 0, 0
	for end in range(len(nums)):
		_sum += nums[end]
		if end >= k - 1: # making equal to the sliding window size
			max_sum = max(_sum, max_sum)  
			_sum -= nums[start]  
			start += 1  # slide the window

	return max_sum



from itertools import combinations

def choose_best_dist(num, k):
	temp = 0
	for i in combinations(num, k):
		temp = max(sum(i), temp)
	return temp


def main():
	arr = [1, 24, 6, -3, 10, -2, 5, 12 ,13]
	#arr = [2,2,2,2,2,2,2,2]
	#arr = [4,3,2,1,6]
	print(sliding_window(arr, 4))
	#print(brute_force(arr))
	print(choose_best_dist(arr, 4))


if __name__ == '__main__':
	main()