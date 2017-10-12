def bubble_sort(list):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(list)):
            if list[j-1] > list[j]:
                swap = False
                list[j-1], list[j] = list[j], list[j-1]
    return list


unsorted_list = [9, 54, 2, 99, 3, 77, 89, 44, 104, 18]

print(bubble_sort(unsorted_list))
