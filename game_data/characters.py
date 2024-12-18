from dataclasses import asdict, fields
from typing import List

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    white_hair: bool = False
    black_hair: bool = False
    red_hair: bool = False
    blonde_hair: bool = False
    brown_hair: bool = False
    mixed_color_hair: bool = False
    beard: bool = False
    moustache: bool = False
    stubble: bool = False
    clean_shaved_face: bool = False
    thick_eyebrows: bool = False
    blushing_cheeks: bool = False
    hat: bool = False
    glasses: bool = False
    earrings: bool = False
    lipstick: bool = False
    bald_head: bool = False
    curls: bool = False
    ponytail: bool = False
    parting: bool = False
    full_head_of_hair: bool = False
    male: bool = False
    female: bool = False
    large_nose: bool = False
    small_nose: bool = False
    blue_eyes: bool = False
    green_eyes: bool = False
    brown_eyes: bool = False
    thin_lips: bool = False
    thick_lips: bool = False
    small_mouth: bool = False
    darker_skin: bool = False
    teeth: bool = False
    dimples: bool = False
    freckles: bool = False
    smile: bool = False


    def __str__(self):
        return self.name

    @property
    def data(self):
        return str(asdict(self))


# TODO: currently we don't allow guessing, but it's easily expandable by allowing "name" to be a trait
TRAITS = [field.name for field in fields(Person) if field.name != 'name']

# Predefined characters
CHARACTERS: List[Person] = [
    Person(name="Audrey", white_hair=True, clean_shaved_face=True, earrings=True, lipstick=True),
    Person(name="Mia", black_hair=True, clean_shaved_face=True, lipstick=True),
    Person(name="Lily", brown_hair=True, clean_shaved_face=True, hat=True, lipstick=True),
    Person(name="Sara", black_hair=True, clean_shaved_face=True, lipstick=True),
    Person(name="Katie", blonde_hair=True, clean_shaved_face=True, hat=True, lipstick=True),
    Person(name="Sophia", brown_hair=True, clean_shaved_face=True, lipstick=True, earrings=True),
    Person(name="Rachel", brown_hair=True, clean_shaved_face=True, glasses=True, earrings=True, lipstick=True),
    Person(name="Olivia", brown_hair=True, mixed_color_hair=True, clean_shaved_face=True, lipstick=True),
    Person(name="Laura", black_hair=True, clean_shaved_face=True, earrings=True, lipstick=True),
    Person(name="Liz", white_hair=True, clean_shaved_face=True, glasses=True, lipstick=True),
    Person(name="Amy", black_hair=True, mixed_color_hair=True, clean_shaved_face=True, glasses=True, lipstick=True),
    Person(name="Jordan", mixed_color_hair=True, beard=True, moustache=True, thick_eyebrows=True, earrings=True),
    Person(name="Mike", black_hair=True, clean_shaved_face=True, blushing_cheeks=True, hat=True),
    Person(name="Leo", white_hair=True, moustache=True),
    Person(name="Sam", black_hair=True, stubble=True, clean_shaved_face=True, thick_eyebrows=True, hat=True),
    Person(name="Daniel", red_hair=True, beard=True, moustache=True, thick_eyebrows=True),
    Person(name="Jo", moustache=True, thick_eyebrows=True, glasses=True),
    Person(name="David", blonde_hair=True, moustache=True, thick_eyebrows=True, hat=True),
    Person(name="Ben", brown_hair=True, stubble=True, clean_shaved_face=True, glasses=True, earrings=True),
    Person(name="Eric", mixed_color_hair=True, clean_shaved_face=True),
    Person(name="Al", white_hair=True, beard=True, moustache=True, thick_eyebrows=True, glasses=True),
    Person(name="Nick", blonde_hair=True, stubble=True, earrings=True),
    Person(name="Lucas", black_hair=True, clean_shaved_face=True),
    Person(name="Emma", red_hair=True, clean_shaved_face=True, blushing_cheeks=True, lipstick=True),
]

print(TRAITS)