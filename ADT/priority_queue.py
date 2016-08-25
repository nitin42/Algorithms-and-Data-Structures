class Priority:
	'''
	>>> pq = Priority()
	>>> pq.insert(('John', 'flu'), 1)
	>>> pq.insert(('Sally', 'cut on arm'), 3)
	>>> pq
	(('John', 'flu'), 1)]
	'''

	def __init__(self):
		self.items = []

	def insert(self, item, p):
		if len(self.items) == 0:
			return self.items.append((item, p))
		for x in range(0, len(self.items)-1):
			if self.items[x][1] < p:
				return self.items.insert(x,(i,p))
		return self.items.append((i, p))

	def peek(self):
		return self.items[0]

	def pop(self):
		if len(self.items) == 0:
			print "Empty"
		return self.items.pop(0)

	def __repr__(self):
		return str(self.items)


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True) 