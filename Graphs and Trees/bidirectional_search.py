# https://en.wikipedia.org/wiki/Bidirectional_search

# Bidirectional search is a graph search algorithm that finds a shortest path from an initial vertex to a goal vertex in a directed graph. 
# Bidirectional search: is used to find the shortest path between a source and destination node. It operates by essentially running two simultaneous breadth-first searches, one from each node. When their searches collide, we have found a path. 


# PSEUDOCODE:
# here is how we solving this problem..
# we are beggining from staring node in right direction and from ending node in left direction in and append the node in the queue.
# the point where both left and right node will be true is the colloding point;
# we will traceback in the path in both direction from the node which has both node.right and node.left == True;

# to trace back we will make a create a new function and traversing through each node by moving right direction in one itteration and moving left in another itteration.

from collections import deque


class Node:
	def __init__(self, data, neighbors=[]):
		self.data = data
		self.neighbors = neighbors
		self.right = None
		self.left = None
		self.visited_right = False
		self.visited_left = False

def bidirectional_search(beg_node, end_node):
	def shortest_path(node):
		"""finding the path after both BFS collide"""
		path = []
		node_copy = node
		while node_copy:
			path.append(node_copy.data)
			node_copy = node_copy.left
		while node:
			path.append(node.data)
			node = node.right
		path.reverse()
		del path[-1]
		return path

	queue = deque([])
	queue.append(beg_node)
	queue.append(end_node)
	beg_node.visited_right = True
	end_node.visited_left = True

	while len(queue) > 0:
		node = queue.pop()

		# spot where both BFS collides.
		if node.visited_right and node.visited_left:
			return shortest_path(node)

		for each_node in node.neighbors:
			# if the search is moving right, make right node == True
			if node.visited_right == True and not each_node.visited_right:
				each_node.right = node
				each_node.visited_right = True
				queue.append(each_node)
			# if the search is moving to left, make left node visited == True
			if node.visited_left == True and not each_node.visited_left:
				each_node.left = node
				each_node.visited_left = True
				queue.append(each_node)
	return False

if __name__ == '__main__':
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n6 = Node(6)
	n7 = Node(7)
	n8 = Node(8)
	n9 = Node(9)
	n10 = Node(10)
	n1.neighbors = [n3, n5]
	n2.neighbors = [n6, n7]
	n3.neighbors = [n2, n8]
	n5.neighbors = [n4, n6]
	n4.neighbors = [n5, n6, n4]
	n6.neighbors = [n7, n9]
	print(bidirectional_search(n1, n7))
#	n0 = Node(0)
#	n1 = Node(1)
#	n2 = Node(2)
#	n3 = Node(3)
#	n4 = Node(4)
#	n5 = Node(5)
#	n6 = Node(6)
#	n7 = Node(7)
#	n0.neighbors = [n1, n5]
#	n1.neighbors = [n0, n2, n6]
#	n2.neighbors = [n1]
#	n3.neighbors = [n4, n6]
#	n4.neighbors = [n3]
#	n5.neighbors = [n0, n6]
#	n6.neighbors = [n1, n3, n5, n7]
#	n7.neighbors = [n6]
#	print(bidirectional_search(n0, n4))


