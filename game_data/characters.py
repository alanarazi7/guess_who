from dataclasses import dataclass
from typing import List


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