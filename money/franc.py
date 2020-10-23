from __future__ import annotations

class Franc:
    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int) -> Franc:
        return Franc(self._amount * multiplier)

    def __eq__(self, franc: Franc):
        return self._amount == franc._amount
