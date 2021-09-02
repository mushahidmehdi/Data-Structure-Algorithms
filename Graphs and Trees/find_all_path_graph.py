# 

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
		return ('No path')
	if start == end:
		return [path]
	paths = []
	for adj in graph[start]:
		if adj not in path:
			new_paths = find_all_path(adj, end, graph, path)
			for pth in new_paths:
				paths.append(pth)
	return paths

print(find_all_path('A', 'D', graph))