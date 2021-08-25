# Terminologies.
# Vertice --> Certain Node on the tree.
# Edge --> Connection b/w Nodes
# Root Node --> The top most node of a tree.
# parent_node, child_node, leaf_node, 


from typing import NewType


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

	def insert(self, data, parent):
		add_node = self.new_node(data)
		
		if self.root is None:
			self.root = add_node
			return add_node
		

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
	root_node = bt.insert(1, None)
	n2 = bt.insert(2, root_node)
	n3 = bt.insert(3, root_node)
	n4 = bt.insert(4, n2)
	n5 = bt.insert(5, n2)
	n6 = bt.insert(6, n3)
	n7 = bt.insert(30000000, n3)
	n7 = bt.insert(337, n4)
	print(bt.root.left.left.left.data)

if __name__ == '__main__':
	test_binary_tree()