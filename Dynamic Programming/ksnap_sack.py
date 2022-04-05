#  Dynamic programming is mostly just a matter of taking a recursive algorithm and finding the overlapping subproblems (that is, the repeated calls). You then cache those results for future recursive calls. As we did in Fabonacci in basics.

# Dynamic Programming: is a set/collection of technique that optimize the algorithm.
# Recurssion
# Memoization/Cacheing
# Bottom-up.

def ksnap_dynamic(items, capacity):
	bag = [0 for i in range(capacity + 1)]
	for i in range(capacity + 1):
		for j in range(len(items)):
			_ , value, weight = items[j]
			if weight < i:
				bag[i] = max(bag[i], bag[i-weight]+value)
	return round(bag[capacity])


def main():
	#items = [('a', 5, 30),('b', 2, 15),('c', .5, 5),('d', 1, 40),
	#('d', 7, 55),('e', 2, 30),('f', 10, 30),('g', 3, 10)]
	items = [('avacado', 2.2, 170),('pomelo', 8, 1500),('durian', 22, 1500),('cucamelon', .26, 15),('lychee', 0.4, 20),('star_apple', 1, 200),]
	print(ksnap_dynamic(items, 2000))


if __name__ == '__main__':
	main()
