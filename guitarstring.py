#!/usr/bin/env python3

from ringbuffer import RingBuffer
import math
import random


class GuitarString:

    # Creates a guitar string given a frequency, using a sampling rate of 44100 Hz
    def __init__(self, frequency: float):
        self.capacity = math.ceil(44100 / frequency)
        self.buffer = RingBuffer(self.capacity)
        for _ in range(self.capacity):
            self.buffer.enqueue(0.0)
        self._time = 0

    @classmethod
    # Creates a guitar string with size and initial values from 'init' array
    def make_from_array(cls, init: list[int]):
        stg = cls(1000)
        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    # Sets the buffer to white noise
    def pluck(self):
        for i in range(self.buffer.size()):
            self.buffer.dequeue()
            self.buffer.enqueue(random.uniform(-0.5, 0.5))

    # Advance the simulation one time step by applying the Karplus--Strong update
    def tick(self):
        first_sample = self.buffer.dequeue()
        second_sample = self.buffer.peek()
        new_sample = 0.996 * 0.5 * (first_sample + second_sample)
        self.buffer.enqueue(new_sample)
        self._time += 1

    # Returns the value of the item at the front of the buffer
    def sample(self) -> float:
        return self.buffer.peek()

    # Returns number of times tick() was called
    def time(self) -> int:
        return self._time