def bubble_sort(n):
    for i in range(len(n)):
        for i in range(len(n) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

numbers = [5, 2, 8, 9, 7]
print(bubble_sort(numbers))
