
# in in-order traveral first left node get traverse followed by visited then at last the right node get traverse.
# Inorder Traversal (left, root, right)

from collections import deque

class Node:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

# using recurrsion
# https://favtutor.com/blogs/tree-traversal-python-with-recursion

def inorder_recurrsive(root):
	stack = []
	inorder_recurrsive_util(root, stack)
	return stack

def inorder_recurrsive_util(root, stack):
	if root is None:
		return
	inorder_recurrsive_util(root.left, stack)
	stack.append(root.data)
	inorder_recurrsive_util(root.right, stack)


def inorder_itterative(root):
	stack = deque()
	cur = root
	while stack or cur:
		if cur:
			stack.append(cur)
			cur = cur.left
		else:
			cur = stack.pop()
			print(cur, end=' ')
			cur = cur.right



if __name__ == '__main__':
	""" Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    """
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.right = Node(6)
	root.right.left = Node(5)
	root.right.left.right = Node(8)
	root.right.left.left = Node(7)
	print(inorder_recurrsive(root))
	print(inorder_itt(root))
