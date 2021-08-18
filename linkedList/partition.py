# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x.
from creatingLinkedList import LinkedList, Node

def partition(ll, k):
	curr = ll.tail = ll.head

	while curr:
		next_node = curr.next
		curr.next = None

		if curr.data < k:
			curr.next = ll.head
			ll.head = curr
		
		else:
			ll.tail.next = curr
			ll.tail = curr
		
		curr = next_node



ll = LinkedList()

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in keys:
	ll.append_beg(Node(i))
partition(ll, 5)
print(ll)

