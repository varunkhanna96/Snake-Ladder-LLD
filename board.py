from dataclasses import dataclass, field
from typing import Dict

from entity import MovingEntity


@dataclass
class Board:
    size: int
    entity_pos: Dict[int, MovingEntity] = field(default_factory=dict)

    def can_move(self, position: int):
        return 1 <= position <= self.size

    def get_next_pos(self, position: int):
        if self.entity_pos.get(position):
            return self.entity_pos[position].end_pos
        else:
            return position

    def reached_end(self, position: int):
        return position == self.size
