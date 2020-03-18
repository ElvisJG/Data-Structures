from doubly_linked_list import doubly_linked_list


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = doubly_linked_list.DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        # return self.storage.length
        return self.size
