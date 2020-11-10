from __future__ import annotations
from typing import TYPE_CHECKING
from money.money import Money
from money.expression import Expression
if TYPE_CHECKING:
    from money.expression import Bank


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def __add__(self, addend: Expression):
        return None

    def reduce(self, bank: Bank, to: str) -> Money:
        amount = self.augend.reduce(
            bank, to)._amount + self.addend.reduce(bank, to)._amount
        return Money(amount, to)
