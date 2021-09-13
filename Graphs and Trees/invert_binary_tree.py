# Inverting binary: To invert a binary tree swap the left to right and right to the left and keep swaping recurrsively.
''' Construct the following tree
			15
		   /  \
		  /    \
		 10      20
		/ \     / \
	   /   \   /   \
	  8    12 16   25

 Inverting the above tree
			15
		   /  \
		  /    \
		 20      10
		/ \     / \
	   /   \   /   \
	  25   16 12    8
'''

class Node:
	def __init__(self, key):
		self.data = key
		self.right = None
		self.left = None

def insert(root, key):
	if root is None:
		return Node(key)
	if key < root.data:
		root.left = insert(root.left, key)
	else:
		root.right = insert(root.right, key)
	return root

def invertion(bt):
	if bt is None:
		return
	bt.right, bt.left = bt.left, bt.right
	invertion(bt.left)
	invertion(bt.right)
	return bt

def main():
	key = [15, 10, 20, 8, 12, 16, 25]
	root = None
	for i in key:
		root = insert(root, i)
	print(root.data)
	invert = invertion(root)
	print(invert.left.data)
	print(invert.right.data)
	print(invert.left.right.data)
	print(invert.left.left.data)

if __name__ == '__main__':
	main()

	
