def binary_search(number, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) //2
        if numbers[mid] == target:
            return numbers[mid] - 1
        elif target > numbers[mid]:
            low = mid + 1
        elif target < numbers[mid]:
            high = mid - 1
    return - 1


numbers = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(numbers, 37))