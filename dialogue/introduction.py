from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
import streamlit as st


def explain_game_and_ask_name():
    # Greeting the player and asking for their name
    play_voice("Hello and welcome to the AI-Powered Guess Who Game! What is your name?")
    player_name = do_speech_to_text()
    st.success(f"Nice to meet you, {player_name}!")
    # TODO: pass my answer to GPT with a prompt, don't hardcode
    play_voice(f"Nice to meet you, {player_name}! Think of a character from the list, and I will try to guess it.")
