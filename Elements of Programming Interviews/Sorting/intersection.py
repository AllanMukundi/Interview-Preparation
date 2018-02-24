def intersection(l1, l2):
    i, j, res = 0, 0, []
    while (i < len(l1) and j < len(l2)):
        if (l1[i] == l2[j]):
            if (len(res) == 0 or res[-1] != l1[i]):
                res.append(l1[i])
            i += 1
            j += 1
        elif (l1[i] > l2[j]):
            j += 1
        else:
            i += 1
    return res

# Unit Tests:
if __name__ == '__main__':
    assert(intersection([], []) == [])
    assert(intersection([0], []) == [])
    assert(intersection([0, 0, 0, 0, 0], [0]) == [0])
    assert(intersection([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10]) == [5, 6, 8])
    assert(intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
