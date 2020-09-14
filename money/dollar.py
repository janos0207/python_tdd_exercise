class Dollar(object):
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier: int):
        self.amount *= multiplier
