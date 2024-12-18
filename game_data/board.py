from dataclasses import dataclass
from secrets import choice
from typing import List

from game_data.characters import Person, TRAITS
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

    def get_non_trivial_trait(self):
        options = []
        for t in TRAITS:
            all_people = [p.has_trait(t) for p in self.remaining]
            if len(set(all_people)) > 1:
                options.append(t)
        trait = choice(options)
        return trait


    def __len__(self) -> int:
        return len(self.remaining)

    def __repr__(self) -> List[str]:
        return [p.name for p in self.remaining]
