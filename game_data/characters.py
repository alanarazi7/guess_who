from dataclasses import asdict, fields
from typing import List, Optional

from dataclasses import dataclass

import pandas as pd
from PIL import Image

from game_data.image import load_image



@dataclass
class Character:
    name: str
    white_hair: bool
    black_hair: bool
    red_hair: bool
    blonde_hair: bool
    brown_hair: bool
    mixed_color_hair: bool
    beard: bool
    moustache: bool
    stubble: bool
    clean_shaved_face: bool
    thick_eyebrows: bool
    blushing_cheeks: bool
    hat_or_hairs_cover: bool
    glasses: bool
    earrings: bool
    lipstick: bool
    bald_head: bool
    curls: bool
    pony_tail: bool
    parting: bool
    full_head_of_hair: bool
    male: bool
    female: bool
    large_nose: bool
    small_nose: bool
    blue_eyes: bool
    green_eyes: bool
    brown_eyes: bool
    thin_lips: bool
    thick_lips: bool
    small_mouth: bool
    darker_skin: bool
    teeths: bool
    dimples: bool
    freckles: bool
    smile: bool
    ear_shown: bool
    image: Optional[Image] = None

    def __post_init__(self):
        self.image = load_image(f"files/individuals/{self.name.lower()}.jpg")


    def __str__(self):
        return self.name

    @property
    def data(self):
        return str(asdict(self))

    def has_trait(self, trait: str) -> bool:
        return getattr(self, trait)

    def get_traits(self, traits: List[str]):
        return {t: self.has_trait(t) for t in traits}

    def has_traits(self, traits: List[str]) -> bool:
        for t in traits:
            if getattr(self, t):
                return True
        return False


def load_characters_df() -> pd.DataFrame:
    df = pd.read_excel("files/Characteristics_Matrix.xlsx", header=1)
    df.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
    df = df[~df['name'].isna()]
    df.columns = [c.lower().strip().replace(" ", "_").replace("'", "") for c in df.columns]
    df.fillna(0, inplace=True)
    for col in df:
        if col != 'name':
            df[col] = df[col].astype(bool)
    return df

characters_df = load_characters_df()
# TODO: currently we don't allow guessing, but it's easily expandable by allowing "name" to be a trait
TRAITS = [c for c in characters_df.columns if c != 'name']

CHARACTERS = []
for _, row in characters_df.iterrows():
    try:
        char = Character(**row.to_dict())
        CHARACTERS.append(char)
    except TypeError as e:
        char_fields = fields(Character)
        raise TypeError(f"{e}: Error creating character: {row.to_dict()}. Expected {char_fields}")
