from doubly_linked_list import doubly_linked_list


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = doubly_linked_list.DoublyLinkedList()

    # Insert
    def enqueue(self, value):
        self.storage.add_to_tail(value)

    # Delete
    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
