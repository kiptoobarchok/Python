#!/usr/bin/python3


def factorial(n):
    """
    Return factorial of n (an exact integer):
    >>> factorial (3)
    6
    >>> [factorial(n) for n in range (6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be an exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n can't be too large

    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be an exact integer")
    if (n+1 == n):
        raise OverflowError("n can't be too large")
    res = 1
    factor = 2
    while factor <= n:
        res *= factor
        factor += 1
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
