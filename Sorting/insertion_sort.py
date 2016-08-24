def insertion_sort(l):
	'''
	>>> l = [1,4,2,12,45,32,3]
	>>> insertion_sort(l)
	[1, 2, 3, 4, 12, 32, 45]
	
	'''

	for i in range(1, len(l)): # Assuming first element is already in sorted place
		key_item = l[i] # Item to be compared and inserted
		j = i

		# Move the elements of the array which are greater than the key elements to one position forward or say shift
		while j >= 0 and key_item < l[j-1]: 
			l[j] = l[j-1] 
			j -= 1

		l[j] = key_item # Move the item to the front

	print l

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)