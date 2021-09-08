# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure. 

# To Solve:
# We will use queue data structure to add and remove instance of the animal;
# Create a linked list and decalare enque and dequeu.

import time

class Node:
	def __init__(self, key):
		self.data = key
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	# queue data structure. FILO: add to the tial
	def add(self, data):
		if self.head is None:
			self.head = data
			return self.head
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = data

	# remove from head
	def remove(self):
		if self.head is None:
			raise ValueError("There is no element in the list")
		remov = self.head
		self.head = self.head.next
		return remov

	def __str__(self):
		nodes = [str(v) for v in self]
		return ' -> '.join(nodes)
	
	def __iter__(self):
		cur = self.head
		while cur:
			yield cur
			cur = cur.next

	def __len__(self):
		cur = self.head
		count = 0
		while cur:
			count += 1
			cur = cur.next

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.admit_date = time.time()

class Cat(Animal):
	pass
class Dog(Animal):
	pass

class AnimalShelter(LinkedList):
	def enqueue(self, data):
		self.add(Node(data))

	def dequeue(self):
		return super().remove()

	def dequeue_dog(self):
		prev = None
		cur = self.head
		while cur:
			if isinstance(cur.data, Dog):
				prev.next = cur.next
				return cur.data
			prev = cur
			cur = cur.next

	def dequeue_cat(self):
		prev = None
		cur = self.head
		while cur:
			if isinstance(cur.data, Cat):
				prev.next = cur.next
				return cur.data
			prev = cur
			cur = cur.next
if __name__ == '__main__':
	animal_shelter = AnimalShelter()
	animal_shelter.enqueue(Dog('Scar-Nose'))
	animal_shelter.enqueue(Cat('Tonny Ginapolist'))
	animal_shelter.enqueue(Dog('Golden Mane'))
	animal_shelter.enqueue(Cat('ScarFace'))
	animal_shelter.enqueue(Cat('MrT'))
	animal_shelter.enqueue(Cat('Rasta'))
	animal_shelter.enqueue(Cat('Pretty Boy'))
	animal_shelter.enqueue(Dog('Dark Mane'))
	animal_shelter.enqueue(Dog('Hip-Scar'))
	animal_shelter.enqueue(Cat('Kinky Tail'))
	animal = animal_shelter.remove()
	dog = animal_shelter.dequeue_dog()
	print(dog.name)




