import random
UNSORTED_LIST_SIZE = 300
MAX_INTEGER_VALUE_FOR_LIST = 1000

# Merges a sorted, left and right list.
def merge(left_list, right_list):
    # Initialize an empty list to consolidate sorted, merged list
    merged_list = []
    i,j = 0, 0
    # Iterate over the left and right lists
    while i < len(left_list) and j < len(right_list):
        # Push the lesser of the two elements into the merged list
        if left_list[i] > right_list[j]:
            merged_list.append(right_list[j])
            j += 1
        else:
            merged_list.append(left_list[i])
            i += 1
    # Iterate over the remaining elements and push into the merged list
    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1
    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1
    return merged_list

# Main Merge sort call
def merge_sort(list):
    if len(list) < 2:
        return list[:]
    else:
        # divide list into two parts and then call merge
        middle = len(list)//2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
        return merge(left, right)

def generate_n_random_elements_in_list(n):
    list = []
    for i in range(0,n):
        list.append(random.randint(1,MAX_INTEGER_VALUE_FOR_LIST))
    return list

#unsorted_list = [9, 54, 17, 2, 99, 3, 77, 89, 44, 104, 18]
unsorted_list = generate_n_random_elements_in_list(UNSORTED_LIST_SIZE)
print("Unsorted list: ")
print(unsorted_list)
print("Sorted List: ")
print(merge_sort(unsorted_list))
