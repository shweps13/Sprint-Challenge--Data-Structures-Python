from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            # print(self.storage.length)
        else:
            if len(self.storage) >= self.capacity:
                # print(self.current, self.storage.tail)
                if self.current is self.storage.tail:
                    self.current = self.storage.head
                    self.storage.head.value = item
                else:
                    self.current.next.value = item
                    self.current = self.current.next

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
        # print(list_buffer_contents)
        return list_buffer_contents

# buffer = RingBuffer(3)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()
# buffer.append('d')

# buffer.get()
# buffer.append('e')
# buffer.append('f')

# buffer.get()

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
