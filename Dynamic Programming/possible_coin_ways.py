# Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. How many possible way we can reach the amount of 7 using the all coin denomination.


def possible_demo_way(array: list, target:int) -> int:
	
	amounts = [0] * (target+1)
	amounts[0] = 1

	for coin in array:
		for amount in range(coin, len(amounts)):
			amounts[amount] += amounts[amount-coin]

	return amounts[target]


def main():
	amounts = [1,2,5]
	print(possible_demo_way(amounts, 7))

if __name__ == '__main__':
	main()
