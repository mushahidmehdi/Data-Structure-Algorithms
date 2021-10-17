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

#def bidirectional_search(src, des):
#	def backtrack(node):
#		path = []
#		copy = node
#		while copy:
#			path.append(copy.data)
#			copy = copy.right
#		while node:
#			path.append(node.data)
#			node = node.left
#		path.reverse()
#		del path[-1]
#		return path
#
#	queue = []
#	queue.append(src)
#	queue.append(des)
#	src.visit_left = True
#	des.visit_right = True
#
#	while len(queue) > 0:
#		node = queue.pop()
#
#		if node.visit_right and node.visit_left:
#			return backtrack(node)
#
#		for neighbor in node.neighbors:
#			if node.visit_right and not neighbor.visit_right:
#				neighbor.right = node
#				neighbor.visit_right = True
#				queue.append(neighbor)
#			if node.visit_left == True and not neighbor.visit_left:
#				neighbor.left = node
#				neighbor.visit_left = True
#				queue.append(neighbor)
#	return False
	

# if __name__ == '__main__':
# 	n1 = Node(1)
# 	n2 = Node(2)
# 	n3 = Node(3)
# 	n4 = Node(4)
# 	n5 = Node(5)
# 	n6 = Node(6)
# 	n7 = Node(7)
# 	n8 = Node(8)
# 	n9 = Node(9)
# 	n10 = Node(10)
# 	n1.neighbors = [n3, n5]
# 	n2.neighbors = [n6, n7]
# 	n3.neighbors = [n2, n8]
# 	n5.neighbors = [n4, n6]
# 	n4.neighbors = [n5, n6, n4]
# 	n6.neighbors = [n7, n9]
# A class to store a BST node

''' Construct the following tree
			15
		   /  \
		  /    \
		 10      20
		/ \     / \
	   /   \   /   \
	  8    12 16   25
'''

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
        self.height = 1

class AvlTree:
    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balanced = self.get_balance(root)

        if balanced > 1 and key > root.left.val:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balanced > 1 and key < root.left.val:
            return self.rotate_right(root)

        if balanced < -1 and key < root.right.val:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        if balanced < -1 and key > root.right.val:
            return self.rotate_left(root)        


        return root

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def rotate_right(self, node):
        y = node.left
        l = y.right
        y.right = node
        node.left = l

        node.height =  1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_left(self, node):
        y = node.right
        l = y.left
        y.left = node
        node.right = l

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return y

    def pre_order(self, node):
        if not node:
            return
        print(f'{node.val}', end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)


if __name__ == '__main__':
    avl_tree = AvlTree()
    root = None
    root = avl_tree.insert(root, 10)
    root = avl_tree.insert(root, 20)
    root = avl_tree.insert(root, 30)
    root = avl_tree.insert(root, 40)
    root = avl_tree.insert(root, 50)
    root = avl_tree.insert(root, 25)
    avl_tree.pre_order(root)

