def insertion_sort(alist):
    """Sorts a list in non-decreasing order."""
    for i in range(1, len(alist)):
        value = alist[i]
        j = i
        while (j > 0 and value < alist[j-1]):
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = value

