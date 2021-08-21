# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list.

#  Write a function that adds the two numbers and returns the sum as a linked list.
#	EXAMPLE
#	Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
#	Output: 2 -> 1 -> 9. That is, 912

from creatingLinkedList import LinkedList

def sum_linked_list(ll1, ll2):
	n1, n2 = ll1, ll2
	ll = NumericLinkedList()
	carry = 0
	while n1 or n2:
		result = carry
		if n1:
			result += n1.value
			n1 = n1.next
		if n2:
			result += n2.value
			n2 = n2.next
		
		ll.add_last(result % 10)
		carry = result // 10
	if carry:
		ll.add_last(carry)
	return ll
		

class NumericLinkedList(LinkedList):
	@classmethod
	def reverse_integers(cls, integers):
		integers = [int(x) for x in str(integers)]
		integers.reverse()
		return cls(integers)


