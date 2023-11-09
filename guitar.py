#!/usr/bin/env python3

from guitarstring import *
from stdaudio import *
import stdkeys

if __name__ == '__main__':
    # Initialize window
    stdkeys.create_window()

    # Define the keyboard mapping and corresponding frequencies
    keyboard = "q2we4r5ty7u8i9op-[=]"
    guitar_strings = []

    # Create a GuitarString for each frequency and appending it to the list
    for i in range(len(keyboard)):
        guitar_strings.append(GuitarString(220.0 * (1.059463 ** (i - 12))))

    # Create a set to keep track of plucked strings
    plucked_strings = set()

    n_iters = 0
    while True:
        # Setting a limit for iterations to avoid bottleneck point
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # Check if client has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                string = guitar_strings[keyboard.index(key)]
                string.pluck()
                plucked_strings.add(string)

        # Compute the superposition of samples only for plucked strings
        sample = 0
        for string in plucked_strings:
            sample += string.sample()

        # Play the sample on standard audio
        play_sample(sample)

        # Advance the simulation of each plucked guitar string by one step
        for string in plucked_strings.copy():  # copy for reference
            string.tick()
            # Remove the string from plucked_strings after 10 seconds and reset the number of
            # ticks to make sure that other plucks of the same string will still play.
            # Checks if buffer is empty to make sure that the reverb happens
            if (string.time() > 8 * 44100) and string.buffer.is_empty():
                plucked_strings.remove(string)
                string._time = 0
