# li = [1,24,5,6,767,8]
# print(li)
# print(li[-1])

# x = isinstance(False, bool)
# print(x)

class Graph:
    # Constructor
    def __init__(self, edges, N):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


if __name__ == '__main__':
	# List of graph edges as per the above diagram

	edges = [# Notice that node 0 is unconnected
	(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
	(3, 5), (8, 9), (8, 12), (9, 10), (9, 11)]

	# total number of nodes in the graph (0–12)
	N = 13

	# build a graph from the given edges
	graph = Graph(edges, N)
	