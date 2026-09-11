def reverse_queue(queue):
    stack = []
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    return queue
        
numberlist = [1, 2, 3, 4]
print(reverse_queue(numberlist))