def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if len(left[i:]) > 0:
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result

def merge_sort(lst):
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]]
    else:
        sorted_left = merge_sort(left_half)
        sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)

print(merge_sort([5, 2, 1, 4, 3]))
