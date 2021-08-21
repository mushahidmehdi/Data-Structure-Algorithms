# remove duplictaes from a LinkedList.

from creatingLinkedList import LinkedList

def remove_duplicates(ll):
	current = ll.head
	prev_node = None
	seen_before = set()

	while current:
		if current.value in seen_before:
			prev_node.next = current.next
		else:
			seen_before.add(current.value)
			prev_node = current
		current = current.next



ll = LinkedList()
keys = [5, 3, 4, 2, 5, 5, 4, 4, 4, 1, 3, 12, 10, 10, 20]
for data in keys:
	ll.add_last(data)
remove_duplicates(ll)

if __name__ == '__main__':
	print(ll)
	
