def twosum_twopointer(lst, target):
    left = 0
    right = len(lst) - 1
    while left < right:
        current_sum = lst[left] + lst[right]
        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
    return None

print(twosum_twopointer([2, 4, 7, 9, 11], 10))