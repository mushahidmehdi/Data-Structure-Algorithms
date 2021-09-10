# Implement a function to check if a binary tree is balanced. For the purposes ofthis question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def get_height(root):
	if root is None: return 0
	return 1 + max(get_height(root.left), get_height(root.right))

def is_balanced(root):
	if root is None: return True
	left_height = get_height(root.left)
	right_height = get_height(root.right)

	if (abs(left_height - right_height) <= 1) and is_balanced(root.left) and is_balanced(root.right):
		return True

	return False

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(0)
	root.left.right = Node(3)
	root.left.left = Node(9)
	root.left.left.right = Node(4)
	root.left.left.left = Node(7)
	root.right = Node(2)
	root.right.left = Node(3)
	root.right.right = Node(4)
	root.right.left.right = Node(5)
	root.right.left.left = Node(5)
	bal = is_balanced(root)
	print(bal)
