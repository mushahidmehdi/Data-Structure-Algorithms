# implement an algorithm to delete a node in the middle but not beggineing & last.

from creatingLinkedList import LinkedList, Node

class DelNode(LinkedList):
	# method 1
	def del_node(self, node):
		prev_node = None
		current = self.head
		while current:
			if current.value == node:
				prev_node.next = current.next
			prev_node = current
			current = current.next
		return self


test_cases = (10, 20, 30, 40, 50)

#	ll = DelNode()
#	for i in test_cases:
#		ll.add_last(i)
#	
#	print(ll.del_node(20))
#	
