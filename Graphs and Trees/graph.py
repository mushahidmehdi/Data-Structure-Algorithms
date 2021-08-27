
# GRAPHS:
# Graphs are networks consisting of nodes connected by edges or arcs. In directed graphs, the connections between nodes have a direction, and are called arcs; in undirected graphs, the connections have no direction and are called edges.
# https://www.python.org/doc/essays/graphs/ 

#graphs are easily built in Python out of lists and dictionaries. For instance, here's a simple graph:

graph = {'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C']
			}