# dijkstra is path finding algorithm which determines the shortest route or path between two nodes, given the cost value of each path.

import math

class Graph:
	def __init__(self, vertices):
		self.dist_arr = [0 for i in range(vertices)]
		self.visited_arr = [0 for i in range(vertices)]
		self.vertices = vertices
		# adjacent metrix graph.
		self.graph = [[0 for column in range(self.vertices)]  for rows in range(self.vertices)]

		def dijkstra(self, src_node):
			for i in range(self.vertices):
				self.dist_arr[i] = math.inf
				self.visited_arr[i] = False
			self.dist_arr[src_node] = 0

			for i in range(self.vertices):
				u = self.min_distance(self.dist_arr, self.visited_arr)
				self.visit_set[u] = True
				

	
	