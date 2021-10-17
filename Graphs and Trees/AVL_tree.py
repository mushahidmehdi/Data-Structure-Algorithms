# AVL Tree Video explaination:
# https://www.youtube.com/watch?v=jDM6_TnYIqE

# AVL is self balancing tree.

class AVLNode:
	def __init__(self, val):
		self.val = val 
		self.right = None
		self.left = None
		self.height = 1

class AVLTree:
	def insert(self, root, key):
		if not root:
			return AVLNode(key)
		if root.val > key:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		root.height = 1 + max(self.get_height(root.left),
		 self.get_height(root.right))

		balanced = self.balance(root)
		
		# balancing cases:
		# Left-Left (LL):
		if balanced > 1 and key < root.left.val:
			return self.pull_right(root)

		# Left-Right (LR):
		if balanced > 1 and key > root.left.val:
			root.left = self.pull_left(root.left)
			return self.pull_right(root)

		# Right-Right (RR):
		if balanced < -1 and key > root.right.val:
			return self.pull_left(root)

		# Right-Left (LR):
		if balanced < -1 and key < root.right.val:
			root.right = self.pull_right(root.right)
			return self.pull_left(root)

		return root
	
	def pull_right(self, node):
		y = node.left
		t = y.right
		y.right = node
		node.left = t

		# new height of y and node:
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
		node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

		return y

	def pull_left(self, node):
		y = node.right
		t1 = y.left
		y.left = node
		node.right = t1

		# new height of y and node:
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
		node.height = 1 + max(self.get_height(node.right), self.get_height(node.left))
		return y

	# getter method to the heigth of tree.
	def get_height(self, root):
		if not root:
			return 0
		return root.height

	# height on both sides of the root node.
	def balance(self, root):
		if not root:
			return 0
		return self.get_height(root.left) - self.get_height(root.right)

	def pre_order(self, root):
		if not root:
			return
		print(f'{root.val}', end=' ')
		self.pre_order(root.left)
		self.pre_order(root.right)


if __name__ == '__main__':
	avl_tree = AVLTree()
	root = None
	root = avl_tree.insert(root, 10)
	root = avl_tree.insert(root, 20)
	root = avl_tree.insert(root, 30)
	root = avl_tree.insert(root, 40)
	root = avl_tree.insert(root, 50)
	root = avl_tree.insert(root, 25)

	avl_tree.pre_order(root)

	# 30 20 10 25 40 50 
	"""
	The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50
	"""


# other self balancing trees
# 1_ Red-black trees
# 2_ Splay trees
# 3_ Treaps