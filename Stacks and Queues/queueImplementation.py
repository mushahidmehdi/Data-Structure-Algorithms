# A Queue is a linear data structure that follows the First In/First Out(FIFO) principle.



class Queue:
	def __init__(self) -> None:
		self.elements = []
	
	def enqueue(self, data):
		self.elements.append(data)

	def dequeue(self):
		return self.elements.pop(0)

	def front(self):
		return self.elements[0]

	def rear(self):
		return self.elements[-1]
	
	def is_empty(self):
		return len(self.elements) == 0


if __name__ == '__main__':
	queue = Queue()
	print(queue.is_empty())
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(4)
	print(queue.front())
	print(queue.rear())
	print(queue.dequeue())

