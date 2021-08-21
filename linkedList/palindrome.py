# Implement a function to check if a linked list is a palindrome.

from creatingLinkedList import LinkedList

def is_palindrome(ll):
	current = ll.head
	stack = []
	while current:
		stack.append(current.value)
		current = current.next
	
	return stack == stack[::-1]

ll = LinkedList()
keys = ['ablewasiereisawelba']
for i in keys: ll.add_last(i)
print(ll)
print(is_palindrome(ll))