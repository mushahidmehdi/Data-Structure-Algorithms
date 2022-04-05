# Dijkstra is path finding algorithm which determines the shortest route or path between two nodes, given the cost value of each path.

# Yhis algorithm used the idea of relaxation which means that
#  d[v] = d[u] + cost(u, v)
# src --> u -- > v 

# Procedure to solve Dijkstra alghorithm in python.
# 1) Create two sets shortest_path -- nodes withs shortest path from source  initially value will be False. Distance -- keep track of Shortest route from source to other nodes, Initialize all distance vaules as infinity bcoz any distance would be less than than inf.

# 2)  Assign distance value as 0 for the source vertex so that we can picked it first.

# 3) While shortest_path doesn’t include all vertices => True: 
# Pick a vertex u which is not there in shortest_path and has minimum distance value, add u to shortest_path.
# Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if the sum of a distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.

from queue import PriorityQueue 

class Graph:
	def __init__(self, vertices) -> None:
		self.vertices = vertices
		self.edges = [[-1 for i in range(vertices)] for i in range(vertices)]
		self.visited = []
	
	def add_edge(self, frm, to, weight):
		self.edges[frm][to] = weight
		self.edges[to][frm] = weight
	
	def dijkstra(self, start):
		dists = {vertice: float('inf') for vertice in range(self.vertices)}
		dists[start] = 0
		proQ = PriorityQueue()
		proQ.put((0, start))

		while (not proQ.empty()):
			dist, current_vertex = proQ.get()
			self.visited.append(current_vertex)

			for neighbor in range(self.vertices):
				if self.edges[current_vertex][neighbor] != -1:
					distance = self.edges[current_vertex][neighbor]
					if neighbor not in self.visited:
						old_cost = dists[neighbor]
						new_cost = dists[current_vertex] + distance
						if new_cost < old_cost:
							proQ.put((distance, neighbor))
							dists[neighbor] = new_cost
		
		return dists



def main():
	node = Graph(9)
	node.add_edge(0, 1, 4)
	node.add_edge(0, 6, 7)
	node.add_edge(1, 6, 11)
	node.add_edge(1, 7, 20)
	node.add_edge(1, 2, 9)
	node.add_edge(2, 3, 6)
	node.add_edge(2, 4, 2)
	node.add_edge(3, 4, 10)
	node.add_edge(3, 5, 5)
	node.add_edge(4, 5, 15)
	node.add_edge(4, 7, 1)
	node.add_edge(4, 8, 5)
	node.add_edge(5, 8, 12)
	node.add_edge(6, 7, 1)
	node.add_edge(7, 8, 3)

	D = node.dijkstra(0)
	for vertex in range(len(D)):
		print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

if __name__ == '__main__':
	main()