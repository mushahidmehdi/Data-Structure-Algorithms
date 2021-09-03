
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def is_binary_search_tree(root, left=None, right=None):
	"""function to check if a binary tree is a binary search tree"""
	# base case
	if root is None: return True
	if(left != None and root.data <= left.data): return False
	if (right != None and root.data >= right.data): return False
	return is_binary_search_tree(root.left, left, root) and  is_binary_search_tree(root.right, root, right)

if __name__ == '__main__':
	root = Node(5)
	root.left = Node(3)
	root.right = Node(6)
	root.left.left = Node(2)
	root.left.right = Node(4)
	#root.right.left = Node(100)
	if is_binary_search_tree(root):
		print('Tree is binary Search Tree')
	else:
		print('Tree isn\'t  binary search tree')
	"""
		5
	  /   \
	 3	   6
    / \	   
   2   4 
	"""