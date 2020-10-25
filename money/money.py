from __future__ import annotations


class Money:
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, money: Money):
        return isinstance(money, type(self)) and self._amount == money._amount
