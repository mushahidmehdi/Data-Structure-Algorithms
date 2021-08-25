# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure. 

import time

class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def __str__(self) -> str:
		return str(self.data)

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, data):
		if self.head is None:
			self.head = data
			return

		current = self.head
		while current.next:
			current = current.next
		current.next = data

	def __len__(self):
		ln = 0
		current = self.head
		while current:
			ln +=1
			current = current.next
		return ln
	
	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __str__(self):
		prt = [str(x.data) for x in self]
		return ' '.join(prt)
		

	def pop_head(self):
		if self.head is not None:
			poping_head = self.head
			self.head = self.head.next
			return poping_head


class Animal:
	def __init__(self, animal_name):
		self.animal_name = animal_name
		self.time_admitted = time.time()

class Cat(Animal):
	pass

class Dog(Animal):
	pass

class AnimalShelter(LinkedList):
	def enqueue(self, animal):
		self.add(Node(animal))

	def deQueue_any(self):
		return super().pop_head()

	def deQueue_cat(self):
		previous = None
		current = self.head
		while current:
			if isinstance(current.data, Cat):
				previous.next = current.next
				return current.data
			previous = current
			current = current.next

	def deQueue_dog(self):
		previous = None
		current = self.head
		while current:
			if isinstance(current.data, Dog):
				previous.next = current.next
				return current.data
			previous = current
			current = current.next


def test_animal_shelter():
	animal_shelter = AnimalShelter()
	animal_shelter.enqueue(Cat('MrT'))
	animal_shelter.enqueue(Cat('Tonny Ginapolist'))
	animal_shelter.enqueue(Cat('Rasta'))
	animal_shelter.enqueue(Cat('ScarFace'))
	animal_shelter.enqueue(Cat('Pretty Boy'))
	animal_shelter.enqueue(Cat('Kinky Tail'))
	animal_shelter.enqueue(Dog('Dark Mane'))
	animal_shelter.enqueue(Dog('Golden Mane'))
	animal_shelter.enqueue(Dog('Scar-Nose'))
	animal_shelter.enqueue(Dog('Hip-Scar'))
	assert len(animal_shelter) == 10
	print(animal_shelter)
	for i in animal_shelter:
		print(i.data)
	


if __name__ == '__main__':
	test_animal_shelter()







