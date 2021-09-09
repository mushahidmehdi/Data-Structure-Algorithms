# li = [1,24,5,6,767,8]
# print(li)
# print(li[-1])

# x = isinstance(False, bool)
# print(x)

# class Graph:
#     # Constructor
#     def __init__(self, edges, N):
#         # A list of lists to represent an adjacency list
#         self.adjList = [[] for _ in range(N)]
#  
#         # add edges to the undirected graph
#         for (src, dest) in edges:
#             self.adjList[src].append(dest)
#             self.adjList[dest].append(src)
# 
# 
# if __name__ == '__main__':
# 	# List of graph edges as per the above diagram
# 
# 	edges = [# Notice that node 0 is unconnected
# 	(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
# 	(3, 5), (8, 9), (8, 12), (9, 10), (9, 11)]
# 
# 	# total number of nodes in the graph (0–12)
# 	N = 13
# 
# 	# build a graph from the given edges
# 	graph = Graph(edges, N)
# 	


#graph = {'A': ['B', 'C'],
#             'B': ['C', 'D'],
#             'C': ['D'],
#             'D': ['C'],
#             'E': ['F'],
#             'F': ['C']}
#
##  Code by Eryk Kopczyński
#from collections import deque
#
#def find_shortest_path(graph, start, end):
#        dist = {start: [start]}
#        q = deque(start)
#        while len(q):
#            at = q.popleft()
#            for next in graph[at]:
#                if next not in dist:
#                    dist[next] = [dist[at], next]
#                    q.append(next)
#        return dist.get(end)
#print(find_shortest_path(graph, 'A', 'D'))
# import numpy as np
#print(np.zeros((9,9)))
# Python program to find the inorder successor in a BST

# Python program to find the inorder successor in a BST

#strg = "  A binary tree node  " 
#str = strg.strip()
#print(str)


class Node:
	def __init__(self , val):
		self.val = val
		self.right = None
		self.left = None
		self.height = 1

class AVLTree:
	def insert(self, root, key):
		if root is None:
			return Node(key)
		if key <= root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		root.height = 1+ max(self.get_height(root.left), self.get_height(root.right))
		balance = self.get_balance(root)

		# Cases:
		if balance > 1 and key < root.left.val:
			return self.pull_right(root)
		if balance > 1 and key > root.left.val:
			root.left = self.pull_left(root.left)
			return self.pull_right(root)

		if balance < -1 and key > root.right.val:
			return self.pull_left(root)
		if balance < -1 and key < root.right.val:
			root.right = self.pull_right(root.right)

		return root

	def pull_right(self, root):
		y = root.left
		t = y.right
		y.right = root
		root.left = t

		root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
		y.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
		return y

	def pull_left(self, root):
		y = root.right
		t = y.left
		y.left = root
		root.right = t

		root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
		y.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

		return y

	def get_height(self, root):
		if not root: return 0
		return root.height

	def get_balance(self, root):
		if not root: return 0
		return self.get_height(root.left) - self.get_height(root.right)

	def pre_order(self, root):
		if not root: return 
		print(f'{root.val}', end=' ')
		self.pre_order(root.left)
		self.pre_order(root.right)
		
if __name__ == '__main__':
	tree = AVLTree()
	root = None
	root = tree.insert(root, 10)
	root = tree.insert(root, 20)
	root = tree.insert(root, 25)
	root = tree.insert(root, 30)
	root = tree.insert(root, 40)
	root = tree.insert(root, 50)
	# tree.pre_order(root)
	print(tree.get_height(root))