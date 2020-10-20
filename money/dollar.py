from __future__ import annotations

class Dollar(object):
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)

    def equals(self, dollar: Dollar):
        return self.amount == dollar.amount
