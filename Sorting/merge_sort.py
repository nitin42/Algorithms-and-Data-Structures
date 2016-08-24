def merge_sort(l):
    
    '''
    >>> l = [1,10,9,2,8,7,4,6,5,3]
    >>> merge_sort(l)
    [1, 10]
    [2, 8]
    [2, 8, 9]
    [1, 2, 8, 9, 10]
    [4, 7]
    [3, 5]
    [3, 5, 6]
    [3, 4, 5, 6, 7]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''

    if len(l) > 1: # Base condition for recursive function
        mid = len(l) // 2 # Obtain the mid index to split the array
        left_sub = l[:mid]
        right_sub = l[mid:]

        merge_sort(left_sub)
        merge_sort(right_sub)

        i = 0
        j = 0
        k = 0

        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] < right_sub[j]:
                l[k] = left_sub[i]
                i += 1

            else:
                l[k] = right_sub[j]
                j += 1

            k += 1

        while i < len(left_sub):
            l[k] = left_sub[i]
            i += 1
            k += 1

        while j < len(right_sub):
            l[k] = right_sub[j]
            j += 1
            k += 1

        print l


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
