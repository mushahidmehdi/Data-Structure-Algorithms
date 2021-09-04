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

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def inOrderSuccessor(n):
	
	# Step 1 of the above algorithm
	if n.right is not None:
		return minValue(n.right)

	# Step 2 of the above algorithm
	p = n.parent
	while( p is not None):
		if n != p.right :
			break
		n = p
		p = p.parent
	return p

# Given a non-empty binary search tree, return the
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
	current = node

	# loop down to find the leftmost leaf
	while(current is not None):
		if current.left is None:
			break
		current = current.left

	return current


# Given a binary search tree and a number, inserts a
# new node with the given number in the correct place
# in the tree. Returns the new root pointer which the
# caller should then use( the standard trick to avoid
# using reference parameters)
def insert( node, data):

	# 1) If tree is empty then return a new singly node
	if node is None:
		return Node(data)
	else:
		
		# 2) Otherwise, recur down the tree
		if data <= node.data:
			temp = insert(node.left, data)
			node.left = temp
			temp.parent = node
		else:
			temp = insert(node.right, data)
			node.right = temp
			temp.parent = node
		
		# return the unchanged node pointer
		return node


# Driver program to test above function

if __name__ == '__main__':
	root = None
	root = insert(root, 20)
	root = insert(root, 4)
	root = insert(root, 12)
	root = insert(root, 10)
	root = insert(root, 14)
	root = insert(root, 8)
	root = insert(root, 22)
	temp = root.left.left
	successor = inOrderSuccessor(temp)
	if successor is not None:
		print( "\nInorder Successor of % d is % d "  %(temp.data, successor.data))
	else:
		print( "\nInorder Successor doesn't exist")


