def count_inversions(arr):
	'''
	>>> count_inversions([1,4,2,5,3])
	3
	'''
	n = len(arr)
	count = 0
	for i in range(n):
		for j in range(i, n):
			if arr[i] > arr[j]:
				count += 1

	return count


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)