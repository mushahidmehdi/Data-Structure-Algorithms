# find nth node from the last of LinkedList.
#For example, if the input is below list and n = 3, then output is “B”
# A -> B -> C -> D

from creatingLinkedList import LinkedList, Node

class KElementFromLast(LinkedList):
	def k_element(self, posi):
		lenght = 0
		temp_node = self.head

		while temp_node:
			lenght += 1
			temp_node = temp_node.next

		if lenght < posi:
			return ("The position is out of range")

		temp_node = self.head
		for _ in range(0, lenght-posi):
			temp_node = temp_node.next
		
		return temp_node.data


ll = KElementFromLast()
ll.append_beg(Node('D'))
ll.append_beg(Node('C'))
ll.append_beg(Node('B'))
ll.append_beg(Node('A'))	
