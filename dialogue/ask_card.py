import streamlit as st

from game_data.characters import CHARACTERS
from game_data.game_state import GameState
from openai_calls.constants import DEBUG_MODE
from openai_calls.prompt2speech import tell_prompt
from openai_calls.speech2text import record_message
from openai_calls.text2text import ask_textually
from utils import normalize_str


def ask_your_card(gs: GameState):
    if DEBUG_MODE:
        st.success(f"Nice to meet you, {gs.player_name}!", icon="👋")
    secret_card_prompt = f'''The player's name is {gs.player_name}. Ask him to pick a character from game board in 
    front of him. Mention you'll use to keep track on the game, and joke about you not going to cheat or peak.'''
    tell_prompt(secret_card_prompt)
    user_choice = record_message(key="user_choice")
    if not user_choice:
        return
    understand_char = f'''The possible names are {[p.name for p in CHARACTERS]}. 
    You asked the kid to pick a character and tell it to you. He said: {user_choice}. 
    Confirm the name of the picked character. Output a JSON with the key `name` and the value being the name'''
    ai_understanding_name = ask_textually(understand_char, force_json=True)

    candidates = [p for p in CHARACTERS if
                  normalize_str(p.name) == normalize_str(ai_understanding_name['name'])]
    if len(candidates) == 1:
        gs.player_char = candidates[0]
    else:
        st.error("Oops! The character name could not be uniquely identified. Please try again.", icon="⚠")