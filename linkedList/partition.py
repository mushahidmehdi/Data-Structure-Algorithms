# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x.

from creatingLinkedList import LinkedList, Node

def partition(ll, k):
	current = ll.tail = ll.head
	while current:
		next_node = current.next
		current.next = None

		if current.value < k:
			current.next = ll.head
			ll.head = current
		else:
			ll.tail.next = current
			ll.tail = current
		current = next_node


ll = LinkedList()
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in keys:
	ll.add_last(i)
partition(ll, 5)
print(ll)

