# linked is are data struce which stores data in a node;
# each node in linkedlists are pointed toward the other node.
# creating a LinkedList

class Node:
    def __init__(self, key, right_node=None, left_node=None) -> str:
        self.data = key
        self.next = right_node
        self.prev = left_node

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        return counter
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        nodes = [str(i) for i in self]
        nodes.append('None')
        return ' -> '.join(nodes)

    def values(self):
        return [vals for vals in self]

    def add_beg(self, key):
        if self.head is None:
            self.tail = self.head = Node(key)
        else:
            self.head = Node(key, self.head)
        return self.head

    def add_last(self, key):
        if self.head is None:
            self.tail = self.head = Node(key)
        else:
            self.tail.next = Node(key)
            self.tail = self.tail.next

    def add_multi(self, keys):
        for key in keys:
            self.add_last(key)

class DoubleLinkedList(LinkedList):
    def add_last(self, key):
        if self.head is None:
            self.tail = self.head = Node(key, self.head)
        else:
            self.tail.next = Node(key, None, self.head)
            self.tail = self.tail.next

    def __str__(self):
        nodes = [str(vals) for vals in self]
        nodes.append('None')
        return ' <=> '.join(nodes)

        

#values = [1,2,3,4,5,6,7,8]
#ll = LinkedList()
#ll.add_multi(values)
#print(ll)
#ll.add_beg(0)
#ll.add_last(9)
#print(len(ll))
#print(ll.values())
#print(ll)
#for i in ll:
#    print(i.data)

#dll = DoubleLinkedList()
#dll.add_multi(values)
#dll.add_last(9)
#print(dll)