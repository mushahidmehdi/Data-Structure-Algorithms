# Let's write a simple function to determine a path between two nodes. It takes a graph and the start and end nodes as arguments. It will return a list of nodes (including the start and end nodes) comprising the path. When no path can be found, it returns None. The same node will not occur more than once on the path returned (i.e. it won't contain cycles). The algorithm uses an important technique called backtracking: it tries each possibility in turn until it finds a solution.

graph = {
		'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C']
			}
def find_path(start, end, graph, path=[]):
	if start not in graph: return None
	path += [start]
	if start == end: return path
	for node in graph[start]:
		if node not in path:
			new_path = find_path(node, end, graph, path)
			return new_path

	return('No path Found')

pth = find_path('A', 'D', graph)
print(pth)