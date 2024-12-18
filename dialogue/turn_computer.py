import streamlit as st

from game_data.board import Board
from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually
from utils import print_ts


def do_computer_turn(board: Board):
    current_board = "\n".join([p.data for p in board.remaining])
    prompt = (
        f'''You are an AI playing a game of guess-who. You are trying to guess the hidden character of your opponent. 
        So far, the remaining characters in the board are the following ones: {current_board}. 
        You have to ask a question to the user to try to guess the character, and it should be a yes/no question. 
        What is your question?''')
    print_ts(f"Planning to ask the user the following prompt: {prompt}")
    ai_question = ask_textually(prompt)
    st.info(f"AI Question: {ai_question}", icon="🤖")
    play_voice(ai_question)
    user_answer = do_speech_to_text()
    st.info(f"User Answer: {user_answer}", icon="👤")
    prompt = (f'''You are an AI playing a game of guess who. This is the board you have right now: {current_board}.
              You asked the user the following question: {ai_question}. The user answered: {user_answer}.
              We now want to filter all the characters that are still possible given the user's answer. 
              What are the characters that are still possible?"
              Answer in a JSON, where keys are the character names, and  values are a boolean if the character is still possible.
              Make sure your JSON includes all the characters, whether they are possible or not.''')
    print_ts(f"Planning to ask the AI the following prompt: {prompt}")
    ai_answer = ask_textually(prompt, force_json=True)
    print_ts(f"AI Answer: {ai_answer}")
    possible_characters = [k for k, v in ai_answer.items() if v]
    board.update_board___(possible_characters=possible_characters)
    return possible_characters