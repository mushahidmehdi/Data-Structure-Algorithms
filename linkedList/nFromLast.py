# find nth node from the last of LinkedList.
#For example, if the input is below list and n = 3, then output is “B”
# A -> B -> C -> D

from creatingLinkedList import LinkedList, Node

class KFromLast(LinkedList):
	def k_frm_last(self, k):
		length = self.__len__()
		temp = self.head
		for _ in range(0, length-k):
			temp = temp.next
		return temp


#test_cases = (10, 20, 30, 40, 50)
#
#ll = KFromLast()
#for x in test_cases:
#	ll.add_last(x)
#
#



