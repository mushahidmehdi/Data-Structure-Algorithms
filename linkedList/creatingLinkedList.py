# creating a LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __len__(self):
        leng = 0
        node = self.head
        while node is not None:
            leng += 1
            node = node.next
        return leng

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append_beg(self, node):
        node.next = self.head
        self.head = node
    
    def append(self, node):
        if self.head is None:
            raise ValueError("Empty List")

        for current in self: pass
        current.next = node
    
    def insert(self, postion, new_node):
        if self.head is None:
            raise ValueError("Empty list")

        for node in self:
            if node.data == postion:
                new_node.next = node.next
                node.next = new_node
                return 
        raise Exception('Position not found')


#
#linked = LinkedList()
#first = Node('a')
#second = Node('b')
#third = Node('c')

#linked.head = first
#first.next = second
#second.next = third
#
#linked.add_beg(Node('B'))
#linked.add_beg(Node('A'))
#
#linked.add_end(Node('X'))
#linked.add_end(Node('Y'))
#linked.add_end(Node('Z'))
#
#linked.add_bt('A', Node('a'))
#linked.add_bt('X', Node('x'))
#linked.add_bt('Z', Node('z'))
#
#
##print(len(linked))
##for i in linked:
##    print(i.data)
#
#print(linked)

keys = [5, 3, 4, 2, 5, 4, 1, 3]
for parm in keys:
   head = Node(parm)
   
