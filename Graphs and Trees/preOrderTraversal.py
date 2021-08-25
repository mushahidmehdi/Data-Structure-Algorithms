# using preOrder traversal, we first traverse through root-node  
# Preorder Traversal (root, left, right)

from collections import deque

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

# recussion
def pre_order_recurssion(data):
	tree_array = []
	pre_order_recurssion_util(data, tree_array)
	return tree_array

def pre_order_recurssion_util(data, tree):
	if data is None:
		return

	tree.append(data.data)
	pre_order_recurssion_util(data.left, tree)
	pre_order_recurssion_util(data.right, tree)
	return

	

# PREORDER ITTERATIVE;
def pre_order_itterative(root):
	if root is None:
		return
	
	stack = deque()
	stack.append(root)

	while stack:
		curr = stack.pop()
		print(curr.data, end=' ')

		if curr.right:
			stack.append(curr.right)
		if curr.left:
			stack.append(curr.left)

if __name__ ==  '__main__':
	node = Node(0)
	node.left = Node(1)
	node.right = Node(2)
	node.left.left = Node(3)
	node.left.right = Node(4)
	node.left.left.left = Node(5)
	node.left.left.right = Node(6)
	node.right.left = Node(7)
	node.right.rigth = Node(8)
	node.right.left.left = Node(9)
	node.right.left.rigth = Node(10)

	print(pre_order_recurssion(node))
	print(pre_order_itterative(node))