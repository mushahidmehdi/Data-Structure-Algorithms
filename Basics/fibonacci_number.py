
#  Emperor Frederick II of Swabia: “How many pairs of rabbits are obtained in a year, excluding cases of death, supposing that each couple gives birth to another couple every month and that the youngest couples are able to reproduce already at the second month of life?”

# https://realpython.com/fibonacci-sequence-python/

# Fabonacci is a quintessential for recursive problem.

def fabonacci_sequence(n):
	"""simplest sol: fobonacci takes O(2**n) run time"""
	if n == 0 or n == 1:
		return n
	else:
		return fabonacci_sequence(n-1) + fabonacci_sequence(n-2)

def fabonnacci(num):
	"""Optimize version using caching:O(n)"""

	# guarded statement.
	if isinstance(num, int) and num >= 0:
		cache = []		# cache will store fib of each #
		cache.append(0)
		cache.append(1)
		size = len(cache)
		for _ in range(size, num+1):
			fibNum = sum(cache[-2:])
			cache.append(fibNum)

		return cache[num]
	else:
		raise ValueError('Please enter: +ve #')


def main():
	print(fabonacci_sequence(5))
	print(fabonnacci(100))

if __name__ == '__main__':
	main()