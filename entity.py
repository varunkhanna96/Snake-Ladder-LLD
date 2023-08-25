from dataclasses import dataclass


@dataclass
class MovingEntity:
    end_pos: int


class Snake(MovingEntity):
    pass


class Ladder(MovingEntity):
    pass
