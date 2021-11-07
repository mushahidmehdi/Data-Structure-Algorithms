# the Floyd–Warshall algorithm is a Dynamic Programming appouch to find shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles). 

# Both Floyd's and Dijkstra's algorithm may be used for finding the shortest path between vertices. The biggest difference is that Floyd's algorithm finds the shortest path between all vertices and Dijkstra's algorithm finds the shortest path between a single vertex and all other vertices.

# Floyed Warshall algorithem fing the shortest path by creating other possible matrix and out of all those choosing the matrix with smallest distance

# formula
# Dk [i , j] = min (Dk-1 [i , j], Dk-1 [i, k] + Dk-1 [k , j])	

import math

def floyd(matrix):
	distance = list(map(lambda p: list(map(lambda q : q, p)), matrix))
	for k in range(Vertices):
		for i in range(Vertices):
			for j in range(Vertices):
				distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
	sol(distance)

def sol(d):
	for i in range(Vertices):
		for j in range(Vertices):
			if d[i][j] == INF:
				print('INF', end=' ')
			else:
				print(d[i][j], end=' ')
		print( )

def main():
	matrix = [
		[0, 5, INF, INF],
        [50, 0, 15, 5],
        [30, INF, 0, 15],
        [15, INF, 5, 0]]
	floyd(matrix)
	


if __name__ == "__main__":
	INF = math.inf
	Vertices = 4
	main()


# https://www.youtube.com/watch?v=oNI0rf2P9gE
# https://favtutor.com/blogs/floyd-warshall-algorithm