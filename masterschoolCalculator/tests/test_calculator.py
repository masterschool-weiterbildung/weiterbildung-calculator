import unittest
from masterschoolCalculator.my_package.calculator import calculate


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate("2+2"), 4)
    def test_addition1(self):
        self.assertEqual(calculate("4+4"), 8)
    def test_subtraction(self):
        self.assertEqual(calculate("4-1"), 3)
    def test_subtraction1(self):
        self.assertEqual(calculate("5-2"), 3)
    def test_multiplication(self):
        self.assertEqual(calculate("1*1"), 1)
    def test_multiplication1(self):
        self.assertEqual(calculate("3*3"), 9)
    def test_division(self):
        self.assertEqual(calculate("9/3"), 3.0)
    def test_division1(self):
        self.assertEqual(calculate("8/2"), 4.0)
    def test_division_remainder(self):
        self.assertEqual(calculate("6~3"), (2,0))
    def test_division_remainder1(self):
        self.assertEqual(calculate("7~3"), (2,1))

if __name__ == '__main__':
    unittest.main()
