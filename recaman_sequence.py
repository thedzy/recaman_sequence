#!/usr/bin/env python3
"""
Script:	recaman_sequence.py
Date:	2020-05-20	

Platform: macOS/Windows/Linux

Description:
Recamán sequence of numbers
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Developer'


def main():
    length = 1000
    max_value = 1000

    # Get sequence of fixed length
    sequence = get_sequence(length)
    print(sequence)
    print('Length', len(sequence))

    # Get sequence until a value (or above is reached)
    sequence = get_sequence(max_value=max_value)
    print(sequence)
    print('Length', len(sequence))


def get_sequence(length=None, max_value=0):
    counter = 0
    sequence = [0]
    while True:
        counter += 1
        digit = sequence[-1] - counter

        if length is None:
            if max_value <= sequence[-1]:
                break
        else:
            if counter > length:
                break

        # If the digit is less than zero or will intersect it move forward
        if digit < 0 or digit in sequence:
            sequence.append(sequence[-1] + counter)
        else:
            sequence.append(sequence[-1] - counter)

    return sequence


if __name__ == '__main__':
    main()
