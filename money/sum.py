from __future__ import annotations
from money.money import Money
from money.expression import Expression


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Money:
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)
