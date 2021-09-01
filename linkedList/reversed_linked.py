# To reverse a linked list, we will initiate three pointers, curr, prev, next as None.
# iterate through the list. while doing so.
# before chaning next to curr
# store next node.
# next = curr.next
# now change the direction of curr to prev
# curr.next = prev
# Move foward.
# prev = curr
# curr = next 

from creatingLinkedList import Node, LinkedList

class ReversedLinkedList(LinkedList):
	def reverse(self):
		prev_node = None
		cur_node = self.head
		while cur_node:
			next_node = cur_node.next
			cur_node.next = prev_node
			prev_node = cur_node
			cur_node = next_node
		self.head = prev_node

if __name__ == '__main__':
	ll = ReversedLinkedList()
	keys = [1,3,5,7,8,9,12,14,15,16]
	for i in keys:
		ll.add_last(Node(i))
	print(ll)
	# 1 -> 3 -> 5 -> 7 -> 8 -> 9 -> 12 -> 14 -> 15 -> 16
	ll.reverse()
	print(ll)
