from dataclasses import dataclass
from secrets import choice
from typing import List

from game_data.characters import Character, TRAITS


@dataclass
class Board:
    remaining: List[Character]


    def update_board(self, traits: List[str], has_traits: bool):
        new_remaining = []
        for p in self.remaining:
            if p.has_traits(traits) == has_traits:
                new_remaining.append(p)
        self.remaining = new_remaining

    def get_non_trivial_trait(self):
        options = []
        for t in TRAITS:
            all_people = [p.has_trait(t) for p in self.remaining]
            if len(set(all_people)) > 1:
                options.append(t)
        trait = choice(options)
        return trait

    @property
    def remaining_msg(self) -> str:
        return f"{len(self.remaining)} Remaining Characters: {str([p.name for p in self.remaining])}"


    def __len__(self) -> int:
        return len(self.remaining)

    def __repr__(self) -> List[str]:
        return [p.name for p in self.remaining]
