def quick_sort(arr):
	
	'''
	>>> quick_sort([11,9,5,7,2,8,1])
	[1,2,5,7,8,9,11]
	
	'''

	merge(arr,0,len(arr)-1) # Quick sort the arr

def merge(arr,first,last):
   if first<last:

       pivot = partition(arr,first,last)

       merge(arr,first,pivot-1)
       merge(arr,pivot+1,last)


def partition(arr,first,last):
   pivotvalue = arr[first]

   left = first+1
   right = last

   flag = False

   while not flag:

       while left <= right and arr[left] <= pivotvalue:
           left = left + 1

       while arr[right] >= pivotvalue and right >= left:
           right = right -1

       if right < left:
           flag = True
       else:
           temp = arr[left]
           arr[left] = arr[right]
           arr[right] = temp

   temp = arr[first]
   arr[first] = arr[right]
   arr[right] = temp

   return right # The split point or the correct position of the pivot value

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
