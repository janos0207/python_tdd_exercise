from __future__ import annotations
from money.expression import Expression


class Money(Expression):
    def __init__(self, amount: int, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, obj: object):
        if isinstance(obj, Money):
            return obj.currency() == self.currency() and self._amount == obj._amount
        return False

    def __repr__(self):
        return "{0} {1}".format(self._amount, self.currency())

    def __add__(self, addend: Money) -> Expression:
        return Money(self._amount + addend._amount, self.currency())

    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")
