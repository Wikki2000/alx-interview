#!/usr/bin/python3
"""
0-minoperations.py
"""


def calc_operations(current, target, ops, copy, is_last_copy):
    """
    Recursive function to calculate the fewest number of operations needed
    to result in exactly n H characters in the file.

    Arguments:
        current (str): The current state of the file.
        target (int): The target length of the file.
        ops (int): The number of operations performed so far.
        copy (str): A copy of the current state of the file.
        is_last_copy (bool): Whether or not the last op was a copy.

    Returns:
        int: The fewest number of operations needed to achieve the
        desired length.
    """
    if len(current) == target:
        # base case: reached the target length, return the number of operations
        return ops
    elif len(current) > target:
        # base case: exceeded the target length, return a very high number
        # of operations to indicate that this is not a viable solution
        return target * 2

    ops += 1  # increment the number of operations

    past = calc_operations(current + copy, target, ops, copy, False)

    copy = target * 2  # if the last one was a copy
    if not is_last_copy:
        copy = calc_operations(current, target, ops, current, True)

    return min(past, copy)  # return the minimum of the two possible solutions


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    The number of operations is the number of times "H" is copied
    to the end of the file, plus the number of times "H" is appended
    to the end of the file.

    If n is less than or equal to 1, the function returns 0.

    Args:
        n (int): The number of H characters in the final file.

    Returns:
        int: The fewest number of operations needed to achieve the
        desired length.

    """
    # base case: if n is less than or equal to 1, return 0
    if n <= 1:
        return 0

    # find the prime factors of n
    # each prime factor corresponds to one copy operation
    primes = 0
    while n != 1:
        for i in range(2, n + 1):
            if (n % i) == 0:
                primes += i
                n = n // i
                break
    return primes
