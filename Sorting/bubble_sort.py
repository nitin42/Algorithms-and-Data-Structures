def bubble_sort(l):
	'''
	>>> l = [1,4,2,12,45,32,3]
	>>> bubble_sort(l)
	[1, 2, 3, 4, 12, 32, 45]

	'''

	for i in range(len(l)-1, 0, -1):
		for j in range(i): # Pass 
			if l[j] > l[j+1]:
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
	print l

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)