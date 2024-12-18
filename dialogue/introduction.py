from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
import streamlit as st

from utils import print_ts


def explain_game_and_ask_name():
    # Greeting the player and asking for their name
    print_ts("Presenting the game and asking for the player's name")
    play_voice("Hello and welcome to the AI-Powered Guess Who Game! What is your name?")
    print(f"Asking name...")
    player_name = do_speech_to_text()
    st.success(f"Nice to meet you, {player_name}!")
    # TODO: pass my answer to GPT with a prompt, don't hardcode
    print(f"Got name, greeting back")
    play_voice(f"Nice to meet you, {player_name}! Think of a character from the list, and I will try to guess it.")
    print(f"Explaining the game...")
