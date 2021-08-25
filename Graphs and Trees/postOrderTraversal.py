# using post-order traversal we fist traverse the left-subtree followed by right-subtree and the parent node respectivly.
# Postorder Traversal (left, right, root)
from collections import deque
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def post_order_recursive(root):
	tree = []
	post_order_recursive_util(root, tree)

	return tree

def post_order_recursive_util(root, tree):
	if root is None:
		return

	post_order_recursive_util(root.left, tree)
	post_order_recursive_util(root.right, tree)
	tree.append(root.data)
	return


def post_order_itterative(root):
	stack = deque()
	out = deque()
	stack.append(root)

	while stack:
		cur = stack.pop()
		out.append(cur.data)

		if cur.left:
			stack.append(cur.left)
		
		if cur.right:
			stack.append(cur.right)
	
	while out:
		print(out.pop(), end=' ')

	



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

	print(post_order_recursive(node))
	print(post_order_itterative(node))
	


