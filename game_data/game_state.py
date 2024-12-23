from dataclasses import dataclass
from typing import Optional

import streamlit as st

from game_data.board import Board
from game_data.characters import Person


@dataclass
class GameState:
    start_game: bool = False
    ai_intro: bool = False
    player_name: Optional[str] = None
    pick_character: bool = False
    player_char: Optional[Person] = None
    ai_char: Optional[Person] = None
    player_board: Optional[Board] = None
    ai_board: Optional[Board] = None
    questions_asked: bool = False
    player_turn: bool = True
    game_over: bool = False

def get_game_state() -> GameState:
    if "game_state" not in st.session_state:
        st.session_state.game_state = GameState()
    return st.session_state.game_state
