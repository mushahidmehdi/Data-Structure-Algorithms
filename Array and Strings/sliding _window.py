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


def main():
	arr = [1, 24, 6, -3, 10, -2, 5, 12 ,13]
	print(brute_force(arr))


if __name__ == '__main__':
	main()