from calc import add, mul, div, sub
import doctest  # Unit test
import unittest

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

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(5, 5), 10)

    def test2(self):
        self.assertEqual(mul(5, 5), 25)

    def test3(self):
        self.assertEqual(mul(5.5, 10), 55.0)

    def test4(self):
        self.assertEqual(div(5, 5), 1.0)

    def test5(self):
        self.assertEqual(div(5, 0), 'Undefined')

    def test6(self):
        self.assertEqual(sub(5, 10), -5)

    def test7(self):
        self.assertEqual(div(6, 8), 0.75)

    def test8(self):
        self.assertEqual(sub(-5, 5), -10)


if __name__=="__main__":
    unittest.main()
    doctest.testmod()