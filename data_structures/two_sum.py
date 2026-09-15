def two_sum(number, n):
    seen = {}
    for i, num in enumerate(numbers):
        complement = n - numbers[i]
        if complement in seen:
            return [complement, numbers[i]]
        else:
            seen[numbers[i]] = i

numbers = [2, 7, 11, 15]
print(two_sum(numbers, 26))