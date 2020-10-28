from __future__ import annotations
from money.money import Money


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Money.franc(self._amount * multiplier)
