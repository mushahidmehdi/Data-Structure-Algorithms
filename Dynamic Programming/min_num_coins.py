# Given an amount and numbers of coins find min number of coins we need whose amount equal to the given amount.
# For instance: Given an amount of $10 how many MINIMUN number if coins from [1,3,4] we need to get the given amount $10.

# We will create a list of length + 1, where each index represent an amount ($)
# Then, if the amount at given index is == or > than the given coin amount.
# We will subtract the index amount from the value of given coin and the difference + 1 index amlounr will be number of coins needed for the given coin.
# we will update the index amount with the min of either the index of index[diff]+1 
# finally return the target index from list amount. if not retuen -1;

# https://www.youtube.com/watch?v=8THI_5SViCQ

def min_num_coins(coins, target):
	amounts = [float('inf') for i in range(target+1) ]
	amounts[0] = 0
	for coin in coins:
		for amount in range(coin, len(amounts)):
			if coin <= amount:
				amounts[amount] = min(amounts[amount], amounts[amount-coin]+ 1)
	
	return amounts[target] if amounts[target] != float('inf') else -1



def main():
	coins = [3,5,7,10]
	target = 150
	print(min_num_coins(coins, target))

if __name__ == '__main__':
	main()