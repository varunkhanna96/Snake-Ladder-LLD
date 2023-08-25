from dataclasses import dataclass


@dataclass
class GamePlayer:
    _id: int
    rank: int = -1
    position: int = 1
