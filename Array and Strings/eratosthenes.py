# given an integer find the prime number for the given number from 0 to n
from math import sqrt

def eratosthenes(n: int):
	primes = [True for i in range(n)]

	primes[0] = False
	primes[1] = False

	num = int(sqrt(n))
	
	for i in range(2, num):
		if primes[i] == True:

			for j in range(i * 2, n, i):
				primes[j] = False
		
	count = 0
	for i in range(len(primes)):
		if primes[i]:
			count += 1
	return count

print(eratosthenes(20))
