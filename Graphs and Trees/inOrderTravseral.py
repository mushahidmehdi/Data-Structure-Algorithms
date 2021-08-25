
# in in-order traveral first left node get traverse followed by visited then at last the right node get traverse.

class Node:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

# using itteration.

# using recurrsion
# https://favtutor.com/blogs/tree-traversal-python-with-recursion

def inOrderTraversal(root):
	answer = []
	inOrderTraversalUtil(root, answer)
	return answer

def inOrderTraversalUtil(root, answer):
	if root is None:
		return

	inOrderTraversalUtil(root.left, answer)
	answer.append(root.data)
	inOrderTraversalUtil(root.right, answer)
	return

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(inOrderTraversal(root))