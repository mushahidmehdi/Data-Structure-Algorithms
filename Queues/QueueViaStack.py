# Implement a MyQueue class which implements a queue using two stacks.

# Method 1 (By making enQueue operation costly) This method makes sure that oldest entered element is always at the top of stack 1, so that deQueue operation just pops from stack1. To put the element at top of stack1, stack2 is used.
# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.
# Here time complexity will be O(n)

class MyQueue:
	def __init__(self):
		self.stack_a = []
		self.stack_b = []

	def enQueue(self, data):
		while len(self.stack_b) != 0:
			self.stack_b.append(self.stack_a[-1])
			self.stack_a.pop()
		self.stack_a.append(data)
		while len(self.stack_b) != 0:
			self.stack_a.append(self.stack_b[-1])
			self.stack_b.pop()

	def deQueue(self):
		if len(self.stack_a) == 0:
			raise Exception(f'Queue is empty..')

		item = self.stack_a[0]
		self.stack_a.pop(0)
		return item

if __name__ == '__main__':
	queue = MyQueue()
	queue.enQueue(1)
	queue.enQueue(2)
	queue.enQueue(3)
	queue.enQueue(4)
	print(queue.deQueue())
	print(queue.deQueue())
	print(queue.deQueue())
	print(queue.deQueue())
