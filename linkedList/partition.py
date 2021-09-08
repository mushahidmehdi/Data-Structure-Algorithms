# Write code to partition a linked list around a value x, such that all nodes less than x come before all
# nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after
# the elements less than x.

# solution:
# we will initiate two pointers one 
from creatingLinkedList import LinkedList


def partition(ll, k):
    current = ll.tail = ll.head

    while current:
        temp = current.next
        current.next = None
        if current.data < k:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = temp


if __name__ == '__main__':
    ll = LinkedList()
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in keys:
        ll.add_last(i)
    partition(ll, 5)
    print(ll)
