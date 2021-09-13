# Level Order Traversal: is a traversing technique in which we visit all the node in tree such a way that after visiting all the nodes at current level, from left to right, then we jump on level below to the current.

# https://www.google.com/search?q=Implement+Level+Order+in+Binary+Tree.&oq=Implement+Level+Order+in+Binary+Tree.&aqs=chrome..69i57.624j0j1&sourceid=chrome&ie=UTF-8#kpvalbx=_ufU-YduBCtSN9u8PsMWzsAI51



# To solve:
# In order to move all the node in the tree in level order traversal; we can used queue data structure, Last In First Out (LIFO): we will begin from root node and enqueue the children of root note right after dequeueing the root node to traverse through the node.

from collections import deque

class Node:
	def __init__(self, key):
		self.data = key
		self.right = None
		self.left = None


def level_order(root):
	if root is None:
		return 
	queue = deque()
	queue.append(root)
	while queue:
		cur = queue.popleft()
		print(f'{cur.data}', end=' ')
		if cur.left:
			queue.append(cur.left)
		if cur.right:
			queue.append(cur.right)

def main():
	root = Node(15)
	root.left = Node(10)
	root.right = Node(20)
	root.left.left = Node(8)
	root.left.right = Node(12)
	root.right.left = Node(16)
	root.right.right = Node(25)
	"""root = Node(1)
	root.left = Node(10)
	root.right = Node(20)
	root.left.right = Node(30)
	root.right.right = Node(40)
	root.left.left = Node(50)
	root.right.left = Node(60)
	root.left.right.left = Node(70)
	root.left.right.right = Node(80)
	root.right.right.left = Node(90)
	root.right.right.right = Node(100)
	root.left.left.right = Node(110)
	root.right.left.left = Node(120)
	"""
	print(level_order(root))



if __name__ == '__main__':
	main()
	


	