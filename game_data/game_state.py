from dataclasses import dataclass

import streamlit as st

@dataclass
class GameState:
    start_game: bool = False
    asked_name: bool = False



def get_game_state() -> GameState:
    if "game_state" not in st.session_state:
        st.session_state.game_state = GameState()
    return st.session_state.game_state


def start_game(gs: GameState):
    if st.button("Start Game!"):
        st.info("Starting the game!", icon="🎉")
        gs.start_game = True