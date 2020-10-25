from __future__ import annotations
from money.money import Money


class Franc(Money):
    def times(self, multiplier: int) -> Money:
        return Franc(self._amount * multiplier)
