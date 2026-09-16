def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = current
    return lst

print(insertion_sort([5, 2, 4, 1, 3]))