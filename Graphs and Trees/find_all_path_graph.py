#  given a graph find all paths given between to given nodes.

graph = {
		'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C']
			}

def find_all_path(start, end, graph, path=[]):
	path = path + [start]
	if start not in graph:
		raise Exception('Please Enter staring point within graph.')
	if start == end:
		return [path]
	paths = []
	for adj in graph[start]:
		if adj not in path:
			new_paths = find_all_path(adj, end, graph, path)
			for pth in new_paths:
				paths.append(pth)
	return paths
if __name__ == '__main__':
	print(find_all_path('A', 'D', graph))