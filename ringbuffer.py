#!/usr/bin/env python3

class RingBuffer:

    # Creating an empty ring buffer given a maximum capacity
    def __init__(self, capacity: int):
        self.MAX_CAP = capacity
        self.buffer = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    # Returns number of items currently in the buffer
    def size(self) -> int:
        return self._size

    # Is the buffer empty (size = 0)?
    def is_empty(self) -> bool:
        return self._size == 0

    # Is the buffer full (size = maximum capacity)?
    def is_full(self) -> bool:
        return self._size == self.MAX_CAP

    # Adds an item 'x' at the end of the buffer
    def enqueue(self, x: float):
        if self.is_full():
            raise RingBufferFull("Buffer is full")
        self.buffer[self._rear] = x
        self._rear = (self._rear + 1) % self.MAX_CAP
        self._size += 1

    # Returns and removes the current item from the front
    def dequeue(self) -> float:
        if self.is_empty():
            raise RingBufferEmpty("Buffer is empty")
        item = self.buffer[self._front]
        self.buffer[self._front] = None

        self._front = (self._front + 1) % self.MAX_CAP
        self._size -= 1
        return item

    # Returns item from the front
    def peek(self) -> float:
        if self.is_empty():
            raise RingBufferEmpty("Buffer is empty")
        return self.buffer[self._front]


# Raises an exception when client attempts to enqueue() into a full buffer
class RingBufferFull(Exception):
    pass


# Raises an exception when client attempts to dequeue() or peek() from an empty buffer
class RingBufferEmpty(Exception):
    pass
