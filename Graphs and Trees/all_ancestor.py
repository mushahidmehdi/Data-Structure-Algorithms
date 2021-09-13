# given a tree find the pedegree (all ancestor nodes) for a given node.

class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


def pedegree(root, node):
	if root is None:
		return 
	
	if root.data == node:
		return True

	if pedegree(root.left, node) or pedegree(root.right, node):
		return (node.data) and 1

	return 0


def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.right.left.right = Node(8)
	root.right.left.left = Node(9)
	root.right.right.left = Node(10)
	root.right.right.right = Node(11)
	return pedegree(root, 11)

if __name__ == '__main__':
	main()


