# ksnap sack is a constrative approuch to maximize the profit while reducing the weight: 
# Both greedy and Dynamic programming can be used to solve this problem.
# x = profit/weight.
# Note: 0/1 knapsack problem is a special case knapsack problem that does not fill the knapsack with fractional items.


# Greedy approuch.
def ksnap_greedy(items, capacity):
	# sort all the items based on highest value/weight ratio.
	items = sorted(items, key= lambda item: item[1]/item[2], reverse=True)
	obj = {}
	profit = 0
	for i in range(len(items)):
		name, value, weight = items[i]
		num_obj = (capacity - capacity % weight)/weight
		obj[name] = num_obj
		capacity = capacity % weight
		profit += num_obj * value
	return round(profit, 2), obj

def main():
	#items = [('a', 5, 30),('b', 2, 15),('c', .5, 5),('d', 1, 40),
	#('d', 7, 55),('e', 2, 30),('f', 10, 30),('g', 3, 10)]
	items = [('avacado', 2.2, 170),('pomelo', 8, 1500),('durian', 22, 1500),('cucamelon', .26, 15),('lychee', 0.4, 20),('star_apple', 1, 200),]
	print(ksnap_greedy(items, 2000))


if __name__ == '__main__':
	main()


# https://www.youtube.com/watch?v=CG7AYoFLN2o
# https://www.w3schools.com/python/ref_func_sorted.asp