class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def count_nodes(head):
    current = head
    count = 0
    while current != None:
        count += 1
        current = current.next
    return count

first = Node(10)
second = Node(20)
third = Node(30)
first.next = second
second.next = third
print(count_nodes(first))