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

print(merge([2, 5], [1, 3, 4]))
