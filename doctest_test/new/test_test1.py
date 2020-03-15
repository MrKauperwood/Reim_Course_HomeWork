#DOCTEST

def lebo(n):
    """
    >>> lebo(0), lebo(1), lebo(8)
    (0, 1, 40320)

    """
    return n*lebo(n-1) if n else 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()