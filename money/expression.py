from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Tuple


class Expression(ABC):
    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Expression:
        pass


class Bank:
    Pair = Tuple[str, str]
    _rates: Dict[Pair, int] = {}

    def reduce(self, source: Expression, to: str) -> Expression:
        return source.reduce(self, to)

    @classmethod
    def add_rate(cls, origin: str, to: str, rate: int):
        cls._rates[(origin, to)] = rate

    @classmethod
    def rate(cls, origin: str, to: str):
        if origin == to:
            return 1
        rate = cls._rates.get((origin, to))
        assert rate is not None
        return rate
