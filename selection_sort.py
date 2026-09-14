def selection_sort(lst):
    for i in range(len(lst)):
        lowest_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[lowest_index]:
                lowest_index = j
        lst[i], lst[lowest_index] = lst[lowest_index], lst[i]
    return lst

print(selection_sort([3, 5, 4, 1, 2]))