def selection_sort(l):
	'''
	>>> l = [1,4,2,12,45,32,3]
	>>> selection_sort(l)
	[1, 2, 3, 4, 12, 32, 45]
	'''
	for i in range(len(l)-1, 0, -1):
		k = 0 # Position of largest element in array
		for j in range(i): # Pass 
			if l[j] > l[k]:
				k = j # Jth position is then largest
		
		# Just exchange the number only once in a pass as compared to bubble sort
		temp = l[i]
		l[i] = l[k]
		l[k] = temp

	print l

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)