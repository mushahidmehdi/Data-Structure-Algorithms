
from collections import deque


def find_shortest_path(start, end, graph, path=[]):
	path = path + [start]
	if start not in graph:
		return ('No path')
	if start == end:
		return path
	shortest = None
	for adj in graph[start]:
		if adj not in path:
			new_paths = find_shortest_path(adj, end, graph, path)
			if new_paths:
				if not shortest or len(new_paths) < len(shortest):
					shortest = new_paths

	return shortest

graph = {
		'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C']
}

print(find_shortest_path('A', 'D', graph))