# X sum problem:  given a list find if there any sub array whose sum would be equal to some other number.
# this problem can be asked as 5-Sum, 4-Sum, 3-Sum, 2-Sum.
# Lets take the example of 3-sum:
# To solve this probelm recurssively, we will reduce the length of the arr by one each time as soon as the counter hit > 3 or lenght of arr == 0; also if the if the target is 0 and counter is 3 then there is a sub array which gives back the k as sum:



def x_sum(arr, _len, count, _sum):
	
	# It work if the count increase by one
	if count == 3 and _sum == 0:
		return True

	if count > 2 or _len == 0:
		return False
	
	return x_sum(arr, _len-1, count + 1, _sum - arr[_len -1]) or x_sum(arr, _len-1, 0, _sum)

def main():
	arr = [3,9,0,0,33,0,0,1]
	_sum = 34
	_len = len(arr)
	ans = x_sum(arr, _len, 0, _sum)
	if ans:
		print(f'There is sub arr whose sum is {_sum}')
	else:
		print('No sub array found')

if __name__ == '__main__':
	main()