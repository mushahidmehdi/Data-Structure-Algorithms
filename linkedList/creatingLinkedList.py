# creating a LinkedList

# init, iter, len, str, values, add_beg, add_last, add mutiple.
import random

class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None

    def __str__(self):
        value = [str(v) for v in self]
        return ' -> '.join(value)

    def __len__(self):
        node = self.head
        ln = 0
        while node:
            ln += 1
            node = node.next
        return ln

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def values(self):
        return [str(x) for x in self]

    def add_beg(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.head = Node(data, self.head)
        return self.head

    def add_last(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def add_mutiple(self, mut):
        for m in mut:
            self.add_last(m)

    @classmethod
    def generate(cls, k, min_val, max_val):
        return cls(random.choices(range(min_val, max_val), k=k))


class DoubleLinkedList(LinkedList):
    def add_last(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data, None, self.tail)
            self.tail = self.tail.next
        return self


#values = [1,2,3,4,5,6,7,8]
#
#ll = LinkedList()
#ll.add_mutiple(values)
#print(ll)
#ll.add_beg(0)
#ll.add_last(9)
#print(len(ll))
#print(ll.values())
#print(ll)
#for i in ll:
#    print(i.value)

#dll = DoubleLinkedList()
#dll.add_mutiple(values)
#dll.add_last(9)
#print(dll)