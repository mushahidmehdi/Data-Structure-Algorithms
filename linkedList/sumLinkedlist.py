# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list.

#  Write a function that adds the two numbers and returns the sum as a linked list.
#	EXAMPLE
#	Input: (1 -> 2 -> 6 -> 9 -> None) + (3 -> 4 -> 2 -> None).
#   That i: 1269 + 342 = 1611
#	Output: 

from creatingLinkedList import LinkedList, Node

class AddTwoLinkedList(LinkedList):
    def add_two_linkedlists(self, ll1, ll2):
        cur1 = ll1.head
        cur2 = ll2.head
        result = Node(0)
        linkedlist = result
        carry = 0
        while cur1 or cur2 or carry:
            val1 = (cur1.data if cur1 else 0)
            val2 = (cur2.data if cur2 else 0)
            carry , out = divmod(val1+val2+carry, 10)
            
            linkedlist.next = Node(out)
            linkedlist = linkedlist.next

            cur1 = (cur1.next if cur1 else None)
            cur2 = (cur2.next if cur2 else None)

        return result.next

                

ll1 = AddTwoLinkedList()
ll2 = AddTwoLinkedList()
ll = AddTwoLinkedList()
ll1.add_multi([1,2,6,9])
ll2.add_multi([3,4,2])
print(ll1)
print(ll2)
print(ll.add_two_linkedlists(ll1, ll2))