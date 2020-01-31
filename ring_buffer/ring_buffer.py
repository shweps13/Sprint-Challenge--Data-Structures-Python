from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            print(self.storage.length)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head

        if self.capacity == 0 or self.capacity is None:
            return []
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        print(list_buffer_contents)
        return list_buffer_contents

buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
