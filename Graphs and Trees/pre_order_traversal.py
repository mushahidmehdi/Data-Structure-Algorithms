# using preOrder traversal, we first traverse the root-node and then left & finally right.  
# Preorder Traversal (root, left, right)

from collections import deque

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

# recussion
def pre_order_recurrsive(root):
	stack = []
	pre_order_recurssive_util(root, stack)
	return stack

def pre_order_recurssive_util(root, stack):
	if root is None:
		return
	
	stack.append(root.data)
	pre_order_recurssive_util(root.left, stack)
	pre_order_recurssive_util(root.right, stack)

def pre_order_itterative(root):
	if root is None:
		return
	stack = deque()
	stack.append(root)
	while stack:
		cur = stack.pop()
		print(cur, end=' ')

		if cur.right:
			stack.append(cur.right)
		if cur.left:
			stack.append(cur.left)

	

if __name__ ==  '__main__':
	node = Node(0)
	node.left = Node(1)
	node.right = Node(2)
	node.left.left = Node(3)
	node.left.right = Node(4)
	node.left.left.left = Node(5)
	node.left.left.right = Node(6)
	node.right.left = Node(7)
	node.right.right = Node(8)
	node.right.left.left = Node(9)
	node.right.left.rigth = Node(10)

	print(pre_order_recurrsive(node))
	#print(pre_order_itterative(node))