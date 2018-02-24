def first_occurrence(nums, target):
    left, right, result = 0, len(nums)-1, -1
    while (left <= right):
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
        else:
            result = mid
            right = mid-1
    return result

# Unit Tests:
if __name__ == '__main__':
    l1 = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    l2 = [10, 10, 10, 10, 10, 10, 10, 10]
    assert(first_occurrence(l1, 108) == 3)
    assert(first_occurrence(l1, 285) == 6)
    assert(first_occurrence(l1, 0) == -1)
    assert(first_occurrence(l1, -10) == 1)
    assert(first_occurrence(l1, 401) == 9)
    assert(first_occurrence(l2, 10) == 0)
    assert(first_occurrence([], 0) == -1)
