def palindrome_queue(queue):
    if len(queue) == 0:
        return "No items in list."
    stack = []
    check = []
    for i in range(len(queue)):
        check.append(queue[i])
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    if queue == check:
        return True
    else:
        return False

numberlist = [1, 2, 3, 2, 1]
print(palindrome_queue(numberlist))
