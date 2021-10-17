# dijkstra is path finding algorithm which determines the shortest route or path between two nodes, given the cost value of each path.

# this algorithm used the idea of relaxation which means that
#  d[v] = d[u] + cost(u, v)
# src--> u -- > v 

# Procedure to solve dijkstra alghorithm in python.
# 1) Create two sets shortest_path -- nodes withs shortest path from source  initially value will be False. Distance -- keep track of Shortest route from source to other nodes, Initialize all distance vaules as infinity bcoz any distance would be less than than inf.

# 2)  Assign distance value as 0 for the source vertex so that we can picked it first.

# 3) While shortest_path doesn’t include all vertices => True: 
# Pick a vertex u which is not there in shortest_path and has minimum distance value, add u to shortest_path.
# Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the sum of a distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.


class Algorithm:
	def __init__(self, vertices):
		self.vertices = vertices
		self.dist = [float('inf')]*vertices
		self.visited = [False]*vertices
		self.matrix = [[0]*vertices]*vertices

	def dijkstra(self, src):
		self.dist[src] = 0
		for _ in range(self.vertices):
			u = self.shortest_path()
			self.visited[u] = True
			for i in range(self.vertices):
				if self.matrix[u][i] > 0 and self.visited[i] == False and self.dist[i] > self.dist[u] + self.matrix[u][i]:
					self.dist[i] = self.dist[u] + self.matrix[u][i]

	def shortest_path(self):
		shortestPath = float('inf')
		for i in range(self.vertices):
			if self.dist[i] < shortestPath and self.visited[i] == False:
				shortestPath = self.dist[i]
				min_index = i
		return min_index

	def print_path(self):
		print('Nodes: \t\t Distance')
		for node in range(self.vertices):
			print(f'{node} \t\t {self.dist[node]}')
		
	def add_edges(self):
		for row in range(self.vertices):
			for col in range(self.vertices):
				edge = int(input(f'Enter edge between ({row},{col}): '))
				self.matrix[col][row] = edge
		return self.matrix

def main():
	algo = Algorithm(6)
	algo.matrix = [[0,2,3,0,0,0],
			  [0,2,0,1,4,0],
			  [3,0,0,5,0,0],
			  [0,1,5,0,0,2],
			  [0,4,0,0,0,3],
			  [0,2,0,0,3,0]
			]
	#algo.add_edges()
	algo.dijkstra(3)
	print(algo.print_path())

if __name__ == '__main__':
	main()
