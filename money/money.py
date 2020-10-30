from __future__ import annotations


class Money:
    def __init__(self, amount: int, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, obj: object):
        if isinstance(obj, Money):
            return obj.currency() == self.currency() and self._amount == obj._amount
        return False

    def __repr__(self):
        return "{0} {1}".format(self._amount, self.currency())

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        from money.dollar import Dollar
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        from money.franc import Franc
        return Franc(amount, "CHF")
