import unittest
from money import Money, Bank
from money.sum import Sum


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
        self.assertEqual("USD", Money.dollar(5).currency)
        self.assertEqual("CHF", Money.franc(5).currency)

    def test_simple_addition(self):
        "Money addition should return new Expression of the total amount."
        total = Money.dollar(5) + Money.dollar(6)
        bank = Bank()
        assert isinstance(total, Sum)
        reduced = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(11), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        six = Money.dollar(6)
        result = five + six
        assert isinstance(result, Sum)
        self.assertEqual(five, result.augend)
        self.assertEqual(six, result.addend)

    def test_reduce_sum(self):
        total = Money.dollar(3) + Money.dollar(4)
        bank = Bank()
        result = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        self.assertEqual(1, Bank.rate("USD", "USD"))

    def test_mixed_addition(self):
        "Bank should reduce a sum of different currencies to a Money of one currency."
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks + ten_francs, "USD")
        self.assertEqual(Money.dollar(10), result)


if __name__ == "__main__":
    unittest.main()
