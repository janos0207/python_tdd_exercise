import unittest
from money import Dollar, Franc

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

    def test_franc_multiplication(self):
        "Multiplication of Francs should return new Franc object of multiplied amount."
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))


if __name__ == "__main__":
    unittest.main()
