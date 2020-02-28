from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    '''
    A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        '''
        adds elements to the buffer
        '''
        # if length of ringbuffer == capacity...
        if self.storage.length == self.capacity:
            # replace oldest element with new item
            self.current = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
                # self.storage.delete(self.current)
                # self.storage.add_to_tail(item)
                # self.current = self.current.prev
        else:
            # add new element to head
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        '''
        returns all of the elements in the buffer in a list in their given order 
        it should not return any `None` values in the list even if they are present in the ring buffer
        '''
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.tail
        # # if element == None...
        while current_node != self.storage.head.prev:
        # returns each element in storage in order until it reaches tail (base)
            if current_node is not None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
