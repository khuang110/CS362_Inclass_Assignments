from calc import add, mul, div, sub
import doctest  # Unit test

# Function to run unit test on calc function
def test():
    """ Returns calculated number

    >>> add(5, 5)
    10

    >>> mul(5, 5)
    25

    >>> mul (5.5, 10)
    55.0

    >>> div(5, 5)
    1.0

    >>> div(5, 0)
    'Undefined'

    >>> sub(5, 10)
    -5

    >>> div(6, 8)
    0.75

    >>> sub(-5, 5)
    -10
    """


if __name__=="__main__":
    doctest.testmod()