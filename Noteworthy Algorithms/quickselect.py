from random import choice as random_choice

def quick_select(elements, k):
    """Returns the kth smallest element in the given list (elements)."""
    if len(elements) == 1:
        return elements[0]
    pivot = random_choice(elements)
    less = []
    greater = []
    for elem in elements:
        if elem < pivot:
            less.append(elem)
        elif elem > pivot:
            greater.append(elem)
    if k <= len(less):
        return quick_select(less, k)
    elif k > len(elements) - len(greater):
        return quick_select(greater, k - (len(elements) - len(greater)))
    else:
        return pivot


# Unit Tests:
if __name__ == '__main__':
    nums = [0, 4, -1, -5, 9, 44, 10, 11, 19]
    assert(quick_select(nums, 1) == -5)
    assert(quick_select(nums, 2) == -1)
    assert(quick_select(nums, 3) == 0)
    assert(quick_select(nums, 4) == 4)
    assert(quick_select(nums, 5) == 9)
    assert(quick_select(nums, 6) == 10)
    assert(quick_select(nums, 7) == 11)
    assert(quick_select(nums, 8) == 19)
    assert(quick_select(nums, 9) == 44)

