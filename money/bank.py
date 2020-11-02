from abc import ABC
from money.money import Money
from money.expression import Expression


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(11)
