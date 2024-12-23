from dataclasses import dataclass
from typing import Optional, List

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
    player_q: Optional[str] = None
    player_q_attempts: int = 0
    ai_turn: bool = False
    ai_trait: Optional[str] = None
    ai_q: Optional[str] = None
    ai_q_user_answer: Optional[str] = None
    game_over: bool = False
    last_turn_was_human: bool = False

def get_game_state() -> GameState:
    if "game_state" not in st.session_state:
        st.session_state.game_state = GameState()
    return st.session_state.game_state
