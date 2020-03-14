from double_linked_list import DoublyLinkedList


# No recursion
# We cannot store the dll and it's data in other data structures
def reverse(dll):
    current = dll.head
    new = current.next
    current.next = None
    while current.next is not None:
        prev = current
        current = new
        current.next = prev
        new = current.next