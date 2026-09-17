def move_zeroes(lst):
    insert_pos = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[insert_pos] = lst[i]
            insert_pos += 1
    for i in range (insert_pos, len(lst)):
        lst[i] = 0
    return lst

print(move_zeroes([0, 1, 0, 3, 12]))