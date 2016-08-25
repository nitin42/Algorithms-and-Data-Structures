class Queue:
	def __init__(self):
		'''
		>>> q = Queue()
		>>> q.enqueue(2)
		>>> q.enqueue(3)
		>>> q.enqueue(4)
		>>> q.dequeue()
		>>> print q.size()
		2
		>>> print q.peek()
		3
		'''
		self.Q = []
		self.head = -1
		self.tail = -1

	def enqueue(self, item):
		if self.head == -1:
			self.head += 1
		self.tail += 1
		self.Q.append(item)

	def dequeue(self):
		if self.head == -1:
			print "Underflow"
		elif self.head == self.tail:
			i = self.Q.pop(0) # Deletes the first item
			self.head += -1
			self.tail += -1
			return i
		else:
			self.tail += 1
			return self.Q.pop(0)

	def size(self):
		return len(self.Q)

	def peek(self):
		if self.head == -1:
			print "Empty queue"
		else:
			return self.Q[self.head]


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
