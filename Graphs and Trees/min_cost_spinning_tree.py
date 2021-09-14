# Given a cyclic graph build a spinning tree which has min edge cost.
# The edges in the graph will always -1 smaller to vertices in the graph.
# Two most popular way to solve this problem are Prims and Kruskal's algorithm:
# Prims algo start building a tree from a smallest value edge and moving to the adjacent next edge which has least value in greedy way.
# Kruskal algorithm used the greedy approuch: chossing the least edges in the graph first without building a cycle again to form spinning tree.

# Implementing Prim's Algorithm:
# this blog expalins the python implementation in very simple and easy way:
# https://stackabuse.com/graphs-in-python-minimum-spanning-trees-prims-algorithm/


import math
def prims_algorithm(vertices):
	# creating adjacent matrix for graph with 0 value.
	adjMtx = [[0 for vertix in range(vertices) ] for vertix in range(vertices)]
	# creating adjacent matrix for MST with 0 value.
	mstMtx = [[0 for vertix in range(vertices)] for vertix in range(vertices)]

	# filling the matrix using python input function.
	for i in range(0, vertices):
	# since adjacent matrix of undirected graph is symmetric therefore we will fill only upper half of diagonal.
		for j in range(0+i, vertices):
			adjMtx[i][j] = int(input(f'Enter path weight b/w vertices({ i },{j}) : '))
			# symmeetic
			adjMtx[j][i] = adjMtx[i][j]

	# Since we are visiting all the vertices, therefore we need to keep track of vertices added into MST, for that we will used list comprehension with a boolen.
	choosenOnes = [False for vertix in range(vertices)]
	# Since we are looking for min spinning tree we need to compare weight of each edge againt very large number.
	inf = math.inf
	while (False in choosenOnes):
		start, end = 0, 0
		minNum = inf
		for i in range(0, vertices):
			if choosenOnes[i]:
				for j in range(0+i, vertices):
					if (not choosenOnes[j] and adjMtx[i][j] > 0):
						if adjMtx[i][j] < minNum:
							minNum = adjMtx[i][j]
							start, end = i, j

		choosenOnes[end] = True
		mstMtx[start][end] = minNum
		if minNum == inf:
			mstMtx[start][end] = 0
			# Symmetric matrix,
		mstMtx[end][start] = mstMtx[start][end]

	print(mstMtx)


if __name__ == '__main__':
	prims_algorithm(5)

	
	
