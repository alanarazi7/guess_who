from dataclasses import dataclass
from typing import List

import pandas as pd


@dataclass
class Person:
    name: str
    hair_color: str
    skin_color: str
    gender: str
    glasses: bool
    facial_hair: bool
    hat: bool
    age: str
    freckles: bool
    jewelry: bool

    def __str__(self):
        return self.name


# Predefined characters
CHARACTERS: List[Person] = [
    Person(name="Laura", hair_color="brown", skin_color="light", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=True),
    Person(name="Mike", hair_color="black", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Lily", hair_color="blue", skin_color="light", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=True),
    Person(name="Sam", hair_color="blonde", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=True, age="young", freckles=False, jewelry=False),
    Person(name="Carmen", hair_color="black", skin_color="dark", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Jordan", hair_color="brown", skin_color="dark", gender="male", glasses=False, facial_hair=True, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Rachel", hair_color="blonde", skin_color="light", gender="female", glasses=True, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Ben", hair_color="brown", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Katie", hair_color="blonde", skin_color="light", gender="female", glasses=False, facial_hair=False, hat=True, age="young", freckles=True, jewelry=False),
    Person(name="Joe", hair_color="black", skin_color="dark", gender="male", glasses=False, facial_hair=True, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Amy", hair_color="black", skin_color="light", gender="female", glasses=True, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Gabe", hair_color="brown", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Emma", hair_color="red", skin_color="light", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=True, jewelry=False),
    Person(name="Al", hair_color="white", skin_color="light", gender="male", glasses=False, facial_hair=True, hat=False, age="old", freckles=False, jewelry=False),
    Person(name="Mia", hair_color="black", skin_color="light", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Leo", hair_color="brown", skin_color="dark", gender="male", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Farah", hair_color="black", skin_color="dark", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=True),
    Person(name="Daniel", hair_color="orange", skin_color="light", gender="male", glasses=False, facial_hair=True, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Sofia", hair_color="brown", skin_color="light", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=True, jewelry=False),
    Person(name="David", hair_color="blonde", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=True, age="young", freckles=False, jewelry=False),
    Person(name="Olivia", hair_color="red", skin_color="dark", gender="female", glasses=False, facial_hair=False, hat=False, age="young", freckles=True, jewelry=False),
    Person(name="Eric", hair_color="blue", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False),
    Person(name="Liz", hair_color="white", skin_color="light", gender="female", glasses=True, facial_hair=False, hat=False, age="old", freckles=False, jewelry=True),
    Person(name="Nick", hair_color="blonde", skin_color="light", gender="male", glasses=False, facial_hair=False, hat=False, age="young", freckles=False, jewelry=False)
]


def characters_to_dataframe(characters):
    data = [{
        "Name": char.name,
        "Hair Color": f"\U0001F9B0 {char.hair_color.capitalize()}",
        "Skin Color": f"\U0001F471 {char.skin_color.capitalize()}",
        "Gender": f"{'\U0001F468 Male' if char.gender == 'male' else '\U0001F469 Female'}",
        "Glasses": "\U0001F453 Yes" if char.glasses else "\U0001F636 No",
        "Facial Hair": "\U0001F9BE Yes" if char.facial_hair else "\U0001F636 No",
        "Hat": "\U0001F9E2 Yes" if char.hat else "\U0001F636 No",
        "Age": f"\U0001F474 {char.age.capitalize()}",
        "Freckles": "\U0001F9B0 Yes" if char.freckles else "\U0001F636 No",
        "Jewelry": "\U0001F48E Yes" if char.jewelry else "\U0001F636 No"
    } for char in characters]
    return pd.DataFrame(data)