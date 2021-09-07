# find nth node from the last of a LinkedList.
# For example, for the below LinkedList and n = 3, then output would be “B”
# A -> B -> C -> D


from creatingLinkedList import LinkedList

def find_n_from_last(ll, node) -> str:
	curr = ll.head
	length = len(ll)
	for _ in range(length - node):
		curr = curr.next
	return curr


#ll = LinkedList()
#ll.add_multi(['A', 'B', 'C', 'D', 'E'])
#print(find_n_from_last(ll, 3))

