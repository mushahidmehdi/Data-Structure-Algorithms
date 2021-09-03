# Terminologies.
# Vertice --> Certain Node on the tree.
# Edge --> Connection b/w Nodes
# Root Node --> The top most node of a tree.
# parent_node, child_node, leaf_node, 


# building a binary tree with python; the binary tree can have only two children nodes.

class Node:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

class BinaryTree:
	new_node = Node
	
	def __init__(self):
		self.root = None

	def insert(self, parent, data):
		add_node = self.new_node(data)
		
		if self.root is None:
			self.root = add_node
			return self.root
		

		if not parent.left:
			parent.left = add_node
			add_node.parent = parent
			
		elif not parent.right:
			parent.right = add_node
			add_node.parent = parent
		else:
			raise Exception('can\'t have more than two nodes')
		
		return add_node


def test_binary_tree():
	bt = BinaryTree()
	root_node = bt.insert(None, 1)
	n2 = bt.insert(root_node, 2)
	n3 = bt.insert(root_node, 3)
	n4 = bt.insert(n2, 4)
	n5 = bt.insert(n2, 5)
	n6 = bt.insert(n3, 6)
	n7 = bt.insert(n3, 7)
	n7 = bt.insert(n4, 10)
	print(bt.root.left.left.left.data)

if __name__ == '__main__':
	test_binary_tree()