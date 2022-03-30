# given two dimentional array find the minumun cost of painting the house
# first draw all the cost tree of the problem.
# second lookup for the repetitive costs
# cash all the repetative costs


def mini_cost(costs: list) ->int:

	lookups = [0, 0, 0]

	for i in range(len(costs)):
		cost_a = costs[i][0] + min(lookups[1], lookups[2])
		cost_b = costs[i][1] + min(lookups[0], lookups[2])
		cost_c = costs[i][2] + min(lookups[0], lookups[1])

		lookups = [cost_a, cost_b, cost_c]
	return min(lookups)

def main():
	arr = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
	arr = [[17, 2, 17], [2, 16, 5], [1, 3, 19]]
	print(mini_cost(arr))

if __name__ == '__main__':
	main()
