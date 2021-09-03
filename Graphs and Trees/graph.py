
# GRAPHS:
# Graphs are networks consisting of nodes connected by edges or arcs. In directed graphs, the connections between nodes have a direction, and are called arcs; in undirected graphs, the connections have no direction and are called edges.
# https://www.python.org/doc/essays/graphs/ 

# graphs are easily built in Python out of lists and dictionaries. For instance, here's a simple graph:
graph = {'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C']
			}

from collections import defaultdict

class Graph:
	def __init__(self):
		self.nodes = set()
		self.arcs = defaultdict(list)
		self.distances = {}

	def add_node(self, node):
		self.nodes.add(node)

	def add_edge(self, from_node, to_node, distance):
		self.arcs[from_node].append(to_node)
		self.distances[(from_node, to_node)] = distance

graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)
graph.add_node(8)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 5, 4)
graph.add_edge(3, 4, 1)
graph.add_edge(3, 7, 6)
graph.add_edge(5, 4, 6)
graph.add_edge(4, 6, 1)
graph.add_edge(6, 8, 4)
graph.add_edge(7, 8, 3)
print(graph)



# Adjacency Matrix Representation
# https://likegeeks.com/python-dijkstras-algorithm/
# https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg

# An adjacency matrix organizes the cost values of edges into rows and columns.
# First, we assign integer indices to our nodes making sure to start our indices at 0. (i.e. A=0, B=1, C=2…).
# We then initialize an N by N array where N is the number of nodes in the graph. We will use NumPy array to build our matrix:
# adjacency_matrix_graph=np.zeros((n,n))
# For instance, element (0,1), corresponding to the number in row 0 column 	, should be filled with the cost value of the edge between nodes 1 and 2 which is 4. We can assign a 5 to element (0,2) with:
# adjacency_matrix_graph[0,2] =  5 (if we use numpy)
# adjacency_matrix_graph[0][1] = 4

adjacency_matrix_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],	
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],	
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
 