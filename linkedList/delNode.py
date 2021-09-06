# implement an algorithm to delete a node in the middle but not beggineing & last.
# To Delete a node from a linked list we need to point pointer of the node before deleting node to the pointer of the pointer of the next node to the delete node;
# 1 -> 2 -> 3 -> 4 -> None (del 2nd node)
# 1 -> 2 -> 3 -> 4 -> None
# 	|_______|
# 1 -> 3 -> 4 -> None

from  creatingLinkedList import LinkedList

def del_middle_node(ll, node):
	curr = ll.head
	prev = None
	while curr:
		if curr.data == node:
			prev.next = curr.next
		prev = curr
		curr = curr.next
	return ll


test_cases = [1,2,3,4,5,6,7,8]
ll = LinkedList()
ll.add_multi(test_cases)
del_node = del_middle_node(ll, 2)
print(del_node)

