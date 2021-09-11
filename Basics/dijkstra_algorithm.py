# dijkstra is path finding algorithm which determines the shortest route or path between two nodes, given the cost value of each path.

# this algorithm used the idea of relaxation which means that
# d[u] + cost(u, v) = d[v]
# src--> u -- > v 

# Procedure to solve dijkstra alghorithm in python.
# 1) Create two sets shortest_path -- nodes withs shorest path from source to distination initially the shortest path will be False, and distance set -- keep track of Shortest route from source to destiney.

# 2) Assign a distance value to all vertices in the input graph.
# Initialize all distance vaules as infinite at the beggining bcoz any distance would be less than than inf. Assign distance value as 0 for the source vertex so that we can picked it first.

# 3) While shortest_path doesn’t include all vertices => True: 
# Pick a vertex u which is not there in shortest_path and has minimum distance value, add u to shortest_path.
# Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the sum of a distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.

import math
import numpy as np

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.shortest_pth = [False] * self.vertices
		self.distance = [math.inf] * self.vertices
		self.graph = np.zeros((6, 6))

	def dijkstra(self, src):
		# initialize the src distance == 0
		self.distance[src] = 0
		for _ in range(self.vertices):
			u = self.shortest_route()
			self.shortest_pth[u] = True
			for i in range(self.vertices):
				if self.graph[u][i] > 0 and self.shortest_pth[i] == False and self.distance[i] > self.distance[u] + self.graph[u][i]:
					self.distance[i] = self.distance[u] + self.graph[u][i]
		print(self.route_printing())

	def shortest_route(self):
		min_val = math.inf
		for i in range(self.vertices):
			if self.distance[i] < min_val and self.shortest_pth[i] == False:
				min_val = self.distance[i]
				min_index = i
		return min_index

	def route_printing(self):
		print('Vertices \tDistances from source')
		for node in range(self.vertices):
			print(node,  "\t\t", self.distance[node])
		

			
if __name__ == '__main__':
	g = Graph(6)
	graphs = [[0,2,3,0,0,0],[0,2,0,1,4,0],
			[3,0,0,5,0,0],[0,1,5,0,0,2],
			[0,4,0,0,0,3],[0,2,0,0,3,0]]
	g.graph = graphs
	g.dijkstra(3)	
	
    

