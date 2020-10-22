import unittest
from money.dollar import Dollar

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        "Multiplication of Dollars should return new Dollar object of multiplied amount."
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_equality(self):
        "Dollars should be equal iff they have same amount."
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))


if __name__ == "__main__":
    unittest.main()
