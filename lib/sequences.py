#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = [
            0,
            1,
        ]

        while len(fib_sequence) < length:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)

        print(fib_sequence)


print_fibonacci(0)
