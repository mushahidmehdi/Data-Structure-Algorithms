# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

# to solve this problem we will create a dictionary; level as a key therefore we will have D keys and list a value and append all node on that level into the list. and used that dictionary to crete new linked lists.

# A class to store a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
 
 
# Function to print a given linked list
def printList(head):
    while head:
        print(head.data, end=" —> ")
        head = head.next
    print("None")
 
# Function to perform inorder traversal on a given binary tree where nodes
# at the same level are linked together in the form of a linked list
def inorder(root):
    if root is None:
        return
    inorder(root.left)
 
    # print current node and its next node
    print(root.data, end=" —> ")
    if root.next:
        print(root.next.data, end='')
    else:
        print("None")
    inorder(root.right)
 
 
# Recursive function to find the first node in the next level of a given root node
def findNextNode(root):
    # base case
    if root is None or root.next is None:
        return None
    # if the left child of the root's next node exists, return it
    if root.next.left:
        return root.next.left
    # if the right child of the root's next node exists, return it
    if root.next.right:
        return root.next.right
    # if root's next node is a leaf node, recur for root's next node
    return findNextNode(root.next)
 
# Recursive function to link nodes present in each level of a binary tree
# in the form of a linked list
def linkNodes(root: Node):
    # base case
    if root is None:
        return
    # ensure that the nodes of the current level are linked before the
    # next level nodes
    linkNodes(root.next)
    # Update the next pointer of root's left child to root's right child.
    # If the right child doesn't exist, link it to the first node in the next level.
    if root.left:
        if root.right:
            root.left.next = root.right
        else:
            root.left.next = findNextNode(root)
 
    # update the next pointer of the root's right child to the first node
    # in the next level
    if root.right:
        root.right.next = findNextNode(root)
    # recur for the left and right subtree
    linkNodes(root.left)
    linkNodes(root.right)
 
if __name__ == '__main__':
 
    ''' Construct the following tree
           1
         /   \
        2     3
       / \     \
      4   5     6
       \       /
        7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.right = Node(7)
    root.right.right.left = Node(8)
 
    # link nodes at the same level
    linkNodes(root)
 
    # print the nodes
    node = root
    while node:
        # print the current level
        printList(node)
 
        # find the leftmost node in the next level
        if node.left:
            node = node.left
        elif node.right:
            node = node.right
        else:
            node = findNextNode(node)
 

