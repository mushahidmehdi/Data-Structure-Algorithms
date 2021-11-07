
#  Emperor Frederick II of Swabia: “How many pairs of rabbits are obtained in a year, excluding cases of death, supposing that each couple gives birth to another couple every month and that the youngest couples are able to reproduce already at the second month of life?”

# https://realpython.com/fibonacci-sequence-python/

# Fabonacci is a quintessential for recursive problem.

def fabonacci_sequence(n):
	"""fobonacci takes O(2**n) run time"""
	# base case to put an end to recurssion.
	if n in {0, 1}:
		return n
	else:
		return fabonacci_sequence(n-1) + fabonacci_sequence(n-2)

# Dynamic Programming 
def fabonnacci(num):
	"""Optimize version using caching:O(n)"""
	# guarded statement.
	if isinstance(num, int) and num >= 0:
		lookUp = []		# lookUp will store fib of each #
		lookUp.append(0)
		lookUp.append(1)
		size = len(lookUp)
		for _ in range(size, num+1):
			fibNum = sum(lookUp[-2:])
			lookUp.append(fibNum)
		return lookUp[num]
	else:
		raise ValueError('Please enter: +ve #')


def main():
	print(fabonacci_sequence(10))
	#print(fabonnacci(100))

if __name__ == '__main__':
	main()