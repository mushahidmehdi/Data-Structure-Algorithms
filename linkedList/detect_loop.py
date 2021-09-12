# To delect a loop in a sequence e.g Linkedlist in this case. We can used a set method in python if the number has seem before then there is a cyle in the sequence, but not for sure!

class Node:
	def __init__(self, key=None, next=None):
		self.data = key
		self.next = next

def cycle(head):
	cur = head
	seem = set()
	while cur:
		if cur.data in seem:
			return True
		seem.add(cur.data)
		cur = cur.next
	return False

# Floyd’s Cycle Detection Algorithm:
# This algorithm allow us to dectec cycle in linked list. We will initiate two ponters at a time one twice fast as another and the if at any position both pointer equalize each other there is a loop. To find the starting point of the loop we will again initaite two pointer one from where both pointer collide each other and one from the head of the linked list, again the positon where both poninter meet each other is the begining of a loop in a linked list. 


def floyd_cycle(head):
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow.data == fast.data:
			return True
	return False


if __name__ == '__main__':
	keys = [1,5,7,9,41,65,56,83,18,8,5,7,9,41,5,56,83,18,8]
	node = None
	for i in keys:
		node = Node(i, node)
	if cycle(node):
		print('Loop Detected')
	else:
		print('Cycle Not Detected')
	if floyd_cycle(node):
		print('Cycle Detected')
	else:
		print('Cycle Not Detected')


# https://www.techiedelight.com/detect-cycle-linked-list-floyds-cycle-detection-algorithm/

# https://www.youtube.com/watch?v=LUm2ABqAs1w