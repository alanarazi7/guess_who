from dataclasses import dataclass
from typing import List

from game_data.characters import Person
from utils import print_ts


@dataclass
class Board:
    remaining: List[Person]


    def update_board(self, traits: List[str], has_traits: bool):
        print_ts(f"There are now {len(self)} possible characters.")
        new_remaining = []
        for p in self.remaining:
            if p.has_traits(traits) == has_traits:
                new_remaining.append(p)
        self.remaining = new_remaining

    def __len__(self) -> int:
        return len(self.remaining)

    def __repr__(self) -> List[str]:
        return [p.name for p in self.remaining]
