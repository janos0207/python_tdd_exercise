from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount: int, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, money: Money):
        return isinstance(money, type(self)) and self._amount == money._amount

    def currency(self) -> str:
        return self._currency

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass

    @staticmethod
    def dollar(amount: int) -> Money:
        from money.dollar import Dollar
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        from money.franc import Franc
        return Franc(amount, "CHF")
