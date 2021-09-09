# every parent node have only two children node and the one on left must be smaller or equal to the parent node and right node must be equal or greater than the parent node, also no two node have same value

class Node:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.right = None
		self.left = None


class BinarySearchTree:
	add_new_node = Node
	def __init__(self):
		self.root = None

	def insert(self, data):
		node = self.add_new_node(data)
		if self.root is None:
			self.root = node
			return 

		current = self.root
		while current:
			if current.data >= data:
				if current.left is None:
					current.left = node
					node.parent = current
					return
				current = current.left
			else:
				if current.right is None:
					current.right = node
					node.parent = current
					return
				current = current.right

		

if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.insert(20)
	bst.insert(9)
	bst.insert(25)
	bst.insert(5)
	bst.insert(12)
	bst.insert(11)
	bst.insert(11)
	bst.insert(11)
	bst.insert(11)
	bst.insert(11)
	bst.insert(11)
	bst.insert(11)

	print(bst.root.right.right.data)