
#DOCTEST


def factorial(n):
    """
    >>> factorial(0), factorial(1), factorial(8)
    (0, 1, 402)

    """
    return n*factorial(n-1) if n else 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()