# BFS starts from a node, then it checks all the nodes at distance one from the beginning node, then it checks all the nodes at distance two, and so on. So as to recollect the nodes to be visited, BFS uses a queue.

# Breadth-First Search is a recursive algorithm to search all the vertices of a graph or a tree. 

#  BFS in python can be implemented by using data structures like a dictionary and lists.


# The steps of the algorithm work as follow:
 # Start by putting any one of the graph’s vertices appending on the queue.
 # Now itterate over the queue: and in every itteration pop the node from front
 # and print:
 # now, check for all neighbours of the given node. if the neighbour isn't in visited list append queue and in visited list.

from collections import deque
def bsf(start, graph):
	queue = [start]		# Last In First Out.
	visited = set()
	visited.add(start)
	while queue:
		node = queue.pop(0)	# first out
		print(node, end=' ')
		for i in graph[node]:
			#if i not in graph:
				#continue
			if i not in visited:
				queue.append(i)
				visited.add(i)
	return visited

if __name__ == '__main__':
	graph = {
		'A': ['B', 'C'],
		'B': ['A', 'E', 'D'],
		'C': ['F', 'G'],
		'E': ['H'],
		'D': [],
		'F': [],
		'G': [],
		'H': [],
	}
	print(bsf('A', graph))


'''
APPLICATIONS:
 In GPS navigation, it helps in finding the shortest path available from one point to another.
 In pathfinding algorithms
 Cycle detection in an undirected graph
 In minimum spanning tree
 To build index by search index
 In Ford-Fulkerson algorithm to find maximum flow in a network.
'''