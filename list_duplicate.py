def find_duplicate(lst):
    seen = set()
    duplicates = set()
    for i in lst:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)

numberlist = [1, 2, 3, 2, 3, 4, 5]
print(find_duplicate(numberlist))