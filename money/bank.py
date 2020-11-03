from money.expression import Expression


class Bank:
    def reduce(self, source: Expression, to: str) -> Expression:
        return source.reduce(to)
