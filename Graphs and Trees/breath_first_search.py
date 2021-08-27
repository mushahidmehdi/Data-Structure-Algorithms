# BFS starts from a node, then it checks all the nodes at distance one from the beginning node, then it checks all the nodes at distance two, and so on. So as to recollect the nodes to be visited, BFS uses a queue.

# Breadth-First Search is a recursive algorithm to search all the vertices of a graph or a tree. 

#  BFS in python can be implemented by using data structures like a dictionary and lists.


# The steps of the algorithm work as follow:

 # Start by putting any one of the graph’s vertices at the back of the queue.
 # Now take the front item of the queue and add it to the visited list.
 # Create a list of that vertex's adjacent nodes. Add those which are not within the visited list to the rear of the queue.
 # Keep continuing steps two and three till the queue is empty.


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def breath_for_search(visited, graph, starting_node):
	# nodes being visited
	visited.append(starting_node)
	queue.append(starting_node)

	while queue:
		node = queue.pop(0)
		print(node, end=' ')
		for adj in graph[node]:
			if adj not in visited:
				visited.append(adj)
				queue.append(adj)



breath_for_search(visited, graph, starting_node='5')


'''
APPLICATIONS:
 In GPS navigation, it helps in finding the shortest path available from one point to another.
 In pathfinding algorithms
 Cycle detection in an undirected graph
 In minimum spanning tree
 To build index by search index
 In Ford-Fulkerson algorithm to find maximum flow in a network.
'''