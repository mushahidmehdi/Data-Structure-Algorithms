# given a tree find the lowest common ancestor.



class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None


def insert(root, key):
    if root is None:
       return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    while root:
        if key < root.data:
            root = root.left
        elif key > root.data:
            root = root.right
        else:
            return True
    return False

def lowest_common_ancestor(root, x, y):
    if root is None or not search(root, x) or not search(root, y):
        return
    cur = root
    while cur:
        if cur.data > max(x, y):
            cur = cur.left
        elif cur.data < min(x, y):
            cur = cur.right
        else:
            return cur
    return cur


def main():
    key = [15, 10, 20, 8, 12, 16, 25]
    root = None
    for i in key:
        root = insert(root, i)
    lca = lowest_common_ancestor(root, 25, 20)
    if lca:
        print("LCA is", lca.data)
    else:
        print("LCA does not exist")

if __name__ == '__main__':
    main()





 