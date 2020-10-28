from __future__ import annotations
from money.money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> Money:
        return Money.dollar(self._amount * multiplier)
