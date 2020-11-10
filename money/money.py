from __future__ import annotations
from typing import TYPE_CHECKING
from money.expression import Expression
if TYPE_CHECKING:
    from money.expression import Bank


class Money(Expression):
    def __init__(self, amount: int, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, obj: object):
        if isinstance(obj, Money):
            return obj.currency == self.currency and self._amount == obj._amount
        return False

    def __repr__(self):
        return "{0} {1}".format(self._amount, self.currency)

    def __add__(self, addend: Expression) -> Expression:
        from money.sum import Sum  # avoid cyclic reference
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        rate = bank.rate(self.currency, to)
        assert rate
        return Money(self._amount // rate, to)

    @property
    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, "CHF")
