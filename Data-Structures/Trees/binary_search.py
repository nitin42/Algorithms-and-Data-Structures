def binary_search(arr, left, right, item):
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

arr = [1,2,3,4,5,6]
item = 5

r = binary_search(arr, 0, len(arr)-1, item)

print r
