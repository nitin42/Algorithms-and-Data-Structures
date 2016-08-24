def binary_search(arr, left, right, item):
	'''
	>>> arr = [1,2,3,4,5,6]
	>>> item = 5
	4
	'''
	
	if right >= left:
		mid = (left + right) / 2

		if arr[mid] == item:
			return mid

		elif arr[mid]>item:
			return binary_search(arr, 1, mid-1, item)

		elif arr[mid]<item:
			return binary_search(arr, mid+1, right, item)

	else:
		return -1

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
