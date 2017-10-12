def binary_search(list, element):
    def binary_search_helper(list, element, low, high):
        if high <= low:
            return list[low] == element
        mid = (low+high)//2
        if element == list[mid]:
            return True
        if element < list[mid]:
            if low == mid:
                return False
            else:
                return binary_search_helper(list, element, low, mid-1)
        else:
            return binary_search_helper(list, element, mid+1, high)
    if len(list) == 0:
        return False
    else:
        return binary_search_helper(list, element, 0, len(list) - 1)

sorted_list = [8, 13, 37, 56, 79, 37, 81, 99, 106, 173]
elements_to_be_searched = [20, 0, 99, 108, -8, 8, 173]

for element in elements_to_be_searched:
    print("Finding {} in {}: {}".format(element, sorted_list, binary_search(sorted_list, element)))

print("Finding {} in {}: {}".format(99, [], binary_search([], 99)))
