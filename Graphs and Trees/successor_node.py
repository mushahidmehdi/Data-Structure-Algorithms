# order successor: gives the next node in the traversal order as in accordce with the traversal types (preOrder-traversal, inOrder-traversal and postOrder-traversal)

#  Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.

"""
		20
	  /   \
	 8	   22
    / \	   
   4   12
  	  / \	   
  	 10   14
"""

# in above tree in inOrder traversal the successor of 8 would be 10, 
# and of 12 would be 14.


# Steps to solve the alghorithm:
# 1) If the right tree of the GIVEN NODE is not None then find the smallest value node on the right subtree.
# 2) If the right subtree of a GIVEN NODE is None, then travel back to its parent node and keep traveling back until we find a new parent with a new right subtree.


class Node:
	def __init__(self, key):
		self.data = key
		self.right = None
		self.left = None

def insert(root, key):
	"""func to add new nodes in BST"""
	# if root is none then create a new node sd as root..
	if root is None:
		return Node(key)
	if key <= root.data:
		root.left =  insert(root.left, key)
	else:
		root.right = insert(root.right, key)
	return root

def find_min(root):
	"""func find min node on the tree"""
	while root.left:
		root = root.left
	return root

def find_successor_node(root, successor, key):
	if root is None: return None
	if root.data == key:
		if root.right:
			return find_min(root.right)
	elif key < root.data:
		successor = root
		return find_successor_node(root.left, successor, key)
	else:
		return find_successor_node(root.right, successor, key)

	return successor


if __name__ == "__main__":
	root = None
	keys = [20, 10, 30, 8, 12, 16, 25]
	for i in keys:
		root = insert(root, i)
	for i in keys:
		pre_successor = find_successor_node(root, None, i)
		if pre_successor:
			print(f'The successor of {i} is {pre_successor.data}')
		else:
			print(f'There is No successor of {i}')



