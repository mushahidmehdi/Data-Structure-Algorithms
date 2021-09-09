# Implementing the idea of FIFO using stacks.
# Implement Queue using two stacks.

# Method 1 (By making enQueue operation costly) This method makes sure that oldest entered element is always at the top of stack 1, so that deQueue operation just pops from stack 1 top. To put the element at top of stack 1, stack 2 will be used. It's like poring from one jar to another.
# While stack1 is not empty, push everything from stack1 to stack2.
# Push new element into stack 1.
# Push everything back to stack 1 from stack 2.
# Here time complexity will be O(n)

class MyQueue:
	def __init__(self):
		self.stack_a = []
		self.stack_b = []

	def enQueue(self, data):
		while len(self.stack_a) != 0:
			self.stack_b.append(self.stack_a.pop())
		self.stack_a.append(data)
		while len(self.stack_b) != 0:
			self.stack_a.append(self.stack_b.pop())
	def deQueue(self):
		if len(self.stack_a) == 0:
			raise Exception(f'Queue is empty..')
		item = self.stack_a.pop()
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
	
