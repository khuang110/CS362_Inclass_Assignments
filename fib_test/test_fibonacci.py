import unittest
import sys
from fibonacci import fib, factorial


def test_answer():
    assert fib(10) == 55


class TestCase(unittest.TestCase):
    # test fibonacci method
    def test1_fib(self):
        self.assertEqual(fib(0), 0)

    def test2_fib(self):
        self.assertEqual(fib(1), 1)

    def test3_fib(self):
        self.assertEqual(fib(2), 1)

    def test4_fib(self):
        self.assertEqual(fib(10), 55)

    def test5_fib(self):
        self.assertEqual(fib(20), 6765)

    ########################################
    ########################################

    # test factorial method
    def test1_fact(self):
        self.assertEqual(factorial(0), 1)

    def test2_fact(self):
        self.assertEqual(factorial(1), 1)

    def test3_fact(self):
        self.assertEqual(factorial(2), 2)

    def test4_fact(self):
        self.assertEqual(factorial(5), 120)

    def test5_fact(self):
        self.assertEqual(factorial(8), 40320)



if __name__=="__main__":
    unittest.main()
