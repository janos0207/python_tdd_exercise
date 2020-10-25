from __future__ import annotations
from abc import abstractmethod


class Money:
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, money: Money):
        return isinstance(money, type(self)) and self._amount == money._amount

    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass

    @staticmethod
    def dollar(amount: int) -> Money:
        from money.dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        from money.franc import Franc
        return Franc(amount)
