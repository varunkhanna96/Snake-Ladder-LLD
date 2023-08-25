import random


class Dice:
    @staticmethod
    def roll() -> int:
        raise NotImplementedError


class SixSideDice(Dice):
    @staticmethod
    def roll() -> int:
        return random.randint(1, 7)
