# X sum problem:  given a list find if there any sub array whose sum would be equal to some other number.
# this problem can be asked as 5-Sum, 4-Sum, 3-Sum, 2-Sum.
# Lets take the example of 3-sum question:
# given a an array find if the sum of three number in array is equal to a target k;

# To solve this probelm recurssively, we will reduce the length of the arr by one each time as soon as the counter hit > 3 or lenght of arr == 0; also if the if the target is 0 and counter is 3 then there is a sub array which gives back the k as sum:


def sum_three(arr, n, count, k):
	
	# base condition 
	if k == 0 and count == 4:
		return True
	# breaking condition for first recursion
	if count > 0 and n == 0:
		return False

	return sum_three(arr, n-1, count + 1, k - arr[n-1]) or sum_three(arr, n-1, count, k)

def main():
	arr = [1,4,6,8,3,6,5,9,1,4,6]
	return sum_three(arr, len(arr), 0, k)

if __name__ == '__main__':
	k = 15
	if main():
		print(f'There is sub arr whose sum is {k}')
	else:
		print('No sub array found')
