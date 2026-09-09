def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        a = lst[0]
        b = find_max(lst[1:])
        biggest = a if a > b else b
        return biggest

print(find_max([2, 5, 9, 7, 6]))