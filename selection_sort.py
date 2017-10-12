def selection_sort(list):
    for i in range(len(list)-1):
        # compare element with every other element after
        # and swap to make this smallest element
        for j in range(i, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j],list[i] # swap
    return list

unsorted_list = [9, 54, 17, 2, 99, 3, 77, 89, 44, 104, 18]

print(selection_sort(unsorted_list))
