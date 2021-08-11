# remove duplictaes from a LinkedList.

from creatingLinkedList import LinkedList
from creatingLinkedList import Node

def remove_duplicates(ll):
	current =  ll.head
	previous = None
	seen = set()

	while current is not None:
		if current.data in seen:
			previous.next = current.next
		else:
			seen.add(current.data)
			previous = current
		current = current.next

	return ll

llist = LinkedList()
keys = sorted([5, 3, 4, 2, 5, 4, 1, 3, 10, 10, 10, 10, 10])

for data in keys:
	llist.append_beg(Node(str(data)))

remove_duplicates(llist)

if __name__ == '__main__':
	print(llist)
	
