from dataclasses import dataclass
from typing import Optional

import streamlit as st

@dataclass
class GameState:
    start_game: bool = False
    ai_intro: Optional[str] = None
    player_recorded_name: bool = False
    player_name: Optional[str] = None



def get_game_state() -> GameState:
    if "game_state" not in st.session_state:
        st.session_state.game_state = GameState()
    return st.session_state.game_state


def start_game(gs: GameState):
    if st.button("Start Game!"):
        st.info("Starting the game!", icon="🎉")
        gs.start_game = True