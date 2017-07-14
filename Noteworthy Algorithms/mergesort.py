def merge(l1, l2):
    """Merges list one (l1) and list two (l2) together in non-decreasing order."""
    result = []
    i = j = 0
    while (i < len(l1) and j < len(l2)):
        if (l1[i] < l2[j]):
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result += l1[i:]
    result += l2[j:]
    return result


def mergeSort(alist):
    """Returns a copy of alist sorted in non-decreasing order."""
    if len(alist) <= 1:
        return alist
    middle = len(alist) // 2
    left = mergeSort(alist[:middle])
    right = mergeSort(alist[middle:])
    return merge(left, right)


def mergeSort_place(alist):
    """Sorts alist in non-decreasing order in-place."""
    if len(alist) > 1:
        middle = len(alist) // 2
        left = alist[:middle]
        right = alist[middle:]

        mergeSort_place(left)
        mergeSort_place(right)

        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if (left[i] < right[j]):
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
            
        while (i < len(left)):
            alist[k] = left[i]
            i += 1
            k += 1

        while (j < len(right)):
            alist[k] = right[j]
            j += 1
            k += 1

