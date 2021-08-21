# Implement a function to check if a linked list is a palindrome.

from creatingLinkedList import LinkedList
class IsPalindrome(LinkedList):
	def is_palindrome(self) -> bool:
		current = self.head
		stack = []
		while current:
			stack.append(current.value)
			current = current.next
		
		return stack == stack[::-1]

ll = IsPalindrome()
keys = ['ablewasiereisawelba']
for i in keys: ll.add_last(i)
print(ll)
print(ll.is_palindrome())