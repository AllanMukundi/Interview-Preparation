def quicksort(alist, a, b):
    """
    Sorts the list from alist[a] to alist[b] inclusive 
    in non-decreasing order using an in-place quick-sort.
    """
    if (a >= b):
        return
    pivot = alist[b]
    left = a
    right = b - 1
    while (left <= right):
        while (left <= right and alist[left] < pivot):
            left += 1
        while(left <= right and pivot < alist[right]):
            right -= 1
        if (left <= right):
            alist[left], alist[right] = alist[right], alist[left]
            left, right = left + 1, right - 1
    alist[left], alist[b] = alist[b], alist[left]
    quicksort(alist, a, left - 1)
    quicksort(alist, left + 1, b) 

def quicksort_copy(alist):
    """Returns a copy of alist in non-decreasing order."""
    if len(alist) <= 1:
        return alist
    less = []
    equal = []
    greater = []
    pivot = alist[0]
    for each in alist:
        if (each < pivot):
            less.append(each)
        elif (each > pivot):
            greater.append(each)
        else:
            equal.append(each)
    return quicksort_copy(less) + equal + quicksort_copy(greater)

