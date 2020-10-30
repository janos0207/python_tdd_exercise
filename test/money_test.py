import unittest
from money import Money


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        "Multiplication of Dollars should return new Dollar object of multiplied amount."
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        "Moneys should be equal iff they have same currency and amount."
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.dollar(5), Money.franc(5))

    def test_currency(self):
        "Money should have their own currency information."
        self.assertEqual("USD", Money.dollar(5).currency())
        self.assertEqual("CHF", Money.franc(5).currency())


if __name__ == "__main__":
    unittest.main()
