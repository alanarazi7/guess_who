from dataclasses import dataclass
from typing import List

from game_data.characters import Person
from utils import print_ts


@dataclass
class Board:
    remaining: List[Person]

    def update_board(self, possible_characters: List[str]):
        print_ts(f"There are now {len(possible_characters)} possible characters.")
        possible_names = {n.lower() for n in possible_characters}
        self.remaining = [p for p in self.remaining if p.name.lower() in possible_names]

    def __len__(self) -> int:
        return len(self.remaining)

    def __repr__(self) -> List[str]:
        return [p.name for p in self.remaining]
