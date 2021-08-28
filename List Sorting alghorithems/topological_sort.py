# typological sort allow us to find all the sub nodes of a given node in acyclic directed graph.

from collections import defaultdict

class TypologicalSort:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def add_edge(self, node, edge):
		return self.graph[node].append(edge)

	def typological_sort_util(self, index, visited, stack):
		visited[index] = True
		for i in self.graph[index]:
			if visited[index] == False:
				self.typological_sort_util(i, visited, stack)
		stack.insert(0, index)

	def typoligical_sort(self):
		visited = [False]*self.vertices
		stack = []
		for index in range(self.vertices):
			if visited[index] == False:
				self.typological_sort_util(index, visited, stack)

		return stack


if __name__ == '__main__':
	graph = TypologicalSort(6)
	graph.add_edge(1, 3)
	graph.add_edge(1, 5)
	graph.add_edge(2, 4)
	graph.add_edge(2, 5)
	graph.add_edge(3, 4)
	graph.add_edge(3, 2)
	graph.add_edge(4, 5)
	graph.add_edge(5, 1)
	graph.add_edge(5, 6)
	print(graph.typoligical_sort())