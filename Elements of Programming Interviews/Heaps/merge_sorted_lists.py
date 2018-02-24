import heapq

def merge_sorted_lists(lists):
    lists = [iter(l) for l in lists]
    heap = []
    for pos, nums in enumerate(lists):
        element = next(nums, None)
        if element is not None:
            heapq.heappush(heap, (element, pos))
    result = []
    while heap:
        smallest, pos = heapq.heappop(heap)
        result.append(smallest)
        element = next(lists[pos], None)
        if element is not None:
            heapq.heappush(heap, (element, pos))
    return result

# Unit Tests:
if __name__ == '__main__':
    l1 = [5, 10, 15, 20]
    l2 = [-3, 0, 18, 19]
    l3 = [-20, -18, -1, 0]
    l4 = [30]
    l5 = [100, 200, 300]
    master_list1 = [l1, l2, l3, l4, l5]
    master_list2 = [l5, l4, l3, l2, l1]
    master_list3 = [l2, l4, l1, l3, l5]
    answer = [-20, -18, -3, -1, 0, 0, 5, 10, 15, 18, 19, 20, 30, 100, 200, 300]
    assert(merge_sorted_lists(master_list1) == answer)
    assert(merge_sorted_lists(master_list2) == answer)
    assert(merge_sorted_lists(master_list3) == answer)
