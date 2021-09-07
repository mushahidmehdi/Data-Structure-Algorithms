# Implement a function to check if a linked list is a palindrome.
# To check whether a LinkedList is palindrome or not take the values of Linked list and compared it aganist reversed slice..

from creatingLinkedList import LinkedList

def is_palindrome(self) -> bool:
	current = self.head
	stack = []
	while current:
		stack.append(current.data)
		current = current.next
	return stack == stack[::-1]

ll = LinkedList()
keys = ['ablewasiereisawelba']
keys = 'mushahid'
for i in keys: ll.add_last(i)
print(ll)
print(is_palindrome(ll))