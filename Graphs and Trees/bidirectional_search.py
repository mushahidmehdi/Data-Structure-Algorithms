
# Bidirectional search: is used to find the shortest path between a source and destination node. It operates by essentially running two simultaneous breadth-first searches, one from each node. When their searches collide, we have found a path. 

class Node:
	def __init__(self, data, neighbors=[]):
		self.data = data
		self.neighbors = neighbors
		self.visited_right = False
		self.visited_left = False
		self.parent_left = None
		self.parent_right = None

from collections import deque

def bidirectional_search(s, t):
	def shortest_path(node):
		"""return the path when both BFS collides"""
		copy_node = node
		path = []
		while node:
			path.append(node.data)
			node = node.parent_right

		path.reverse()
		del path[-1]

		while copy_node:
			path.append(copy_node.data)
			copy_node = copy_node.parent_left

		return path
	queue = deque([])
	queue.append(s)
	queue.append(t)
	s.visited_right = True
	t.visited_left = True

	while len(queue) > 0:
		n = queue.pop()
		if n.visited_left and n.visited_right:
			return shortest_path(n)
		
		for node in n.neighbors:
			if n.visited_left == True and not node.visited_left:
				node.parent = n
				node.visited_left = True
				queue.append(node)
			if n.visited_right == True and not node.visited_right:
				node.parent = n
				node.visited_right = True
				queue.append(node)

	return False


if __name__ == '__main__':
	n0 = Node(0)
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n6 = Node(6)
	n7 = Node(7)
	n0.neighbors = [n1, n5]
	n1.neighbors = [n0, n2, n6]
	n2.neighbors = [n1]
	n3.neighbors = [n4, n6]
	n4.neighbors = [n3]
	n5.neighbors = [n0, n6]
	n6.neighbors = [n1, n3, n5, n7]
	n7.neighbors = [n6]
	print(bidirectional_search(n0, n4))







			


