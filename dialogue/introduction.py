from dialogue.system_message import SYS_MSG
from game_data.game_state import GameState
from openai_calls.speech2text import record_message
from openai_calls.text2speech import play_voice
import streamlit as st

from openai_calls.text2text import ask_textually


def explain_game_and_ask_name(gs: GameState):
    opening_prompt = (f"{SYS_MSG}. Welcome the kid to the game, and explain in one sentences what are the rules of "
                      f"Guess Who. End by asking the kid's name")
    if not gs.ai_intro:
        gs.ai_intro = ask_textually(opening_prompt)
    if gs.ai_intro and not gs.player_recorded_name:
        play_voice(gs.ai_intro)
        player_name = record_message(key="player_name")
        name_recognition_prompt = (f"You asked for a kid's name, and he said it's: {player_name}."
                               f"Confirm the name. Output a JSON with the key `name` and the value being the name")
        ai_name_recognition = ask_textually(name_recognition_prompt, force_json=True)
        gs.player_name = ai_name_recognition['name']
