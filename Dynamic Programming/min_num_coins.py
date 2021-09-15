# Given an amount and numbers of coins find min number of coins we need whose amount equal to the given amount.
# For instance: Given an amount of $10 how many MINIMUN number if coins from [1,3,4] we need to get the given amount $10.

# We will use Dynamic coding for this purpose.
# we will create list amounts: len == num of coins + 1,
# Given an index from 0 to 10 if the index < == the amount of given coin we will simply subtract the index from given coin unit amount, and the difference will be added to the 1 coin.
# index - 1(amount of given coint) == new_index
# new_index amount from add 1 coin will be filled to the index.
# arr[amount] = min(arr[amount], arr[amout - denom] + 1)
# Run time complexity is quadratic.
# https://www.youtube.com/watch?v=8THI_5SViCQ

def min_num_coins(target, coins):
	amounts = [float('inf') for i in range(target + 1)]
	amounts[0] = 0
	for coin in coins:
		for amount in range(len(amounts)):
			if coin <= amount:
				amounts[amount] = min(amounts[amount], 1 +amounts[amount-coin])

	return amounts[target] if amounts[target] != float('inf') else -1

def main():
	coins = [3,5,7,10]
	target = 150
	print(min_num_coins(target, coins))

if __name__ == '__main__':
	main()