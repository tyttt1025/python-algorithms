class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head
    while current != None:
        print(current.value)
        current = current.next

first = Node(10)
second = Node(20)
third = Node(30)
first.next = second
second.next = third

print_list(first)