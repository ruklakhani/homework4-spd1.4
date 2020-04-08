# Find the middle item in a singly linked list, or two 
# middle items if it contains an even number of nodes.
from linkedlist import LinkedList, Node

def find_middle(linked_list):
    even = False 
    mid = linked_list.length() // 2 
    if linked_list.length()%2 == 0:
        even = True 
        mid -= 1
    node = linked_list.head
    counter = 0 
    while node is not None:
        if mid == counter:
            if even: 
                return [node.data, node.next.data]
            return [node.data]
        counter += 1
        node = node.next

testlist = LinkedList([5, 6, 8, 13, 24, 40])

print(find_middle(testlist))

testlist = LinkedList([3, 4, 7, 15, 27, 32, 76])

print(find_middle(testlist))