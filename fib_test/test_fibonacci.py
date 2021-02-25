import unittest
from fibonacci import fib


def test_answer():
    assert fib(10) == 55


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fib(0), 0)

    def test2(self):
        self.assertEqual(fib(1), 1)

    def test3(self):
        self.assertEqual(fib(2), 1)

    def test4(self):
        self.assertEqual(fib(10), 55)

    def test5(self):
        self.assertEqual(fib(20), 6765)


if __name__=="__main__":
    print(fib(10))
    unittest.main()
