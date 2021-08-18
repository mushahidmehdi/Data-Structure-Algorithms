# implement an algorithm to delete a node in the middle but not beggineing & last.

from creatingLinkedList import LinkedList, Node

class DelMiddleNode(LinkedList):
	def pop(self, pos):
		
		previous = self.head
		for current in self:
			if current.data == pos and current.next != None:
				previous.next = current.next
			previous = current
		
		




ll = DelMiddleNode()
ll.append_beg(Node('D'))
ll.append_beg(Node('C'))
ll.append_beg(Node('B'))
ll.append_beg(Node('A'))
print(f'before Delete: {ll}')
ll.pop('D')
print(f'After Delete: {ll}')