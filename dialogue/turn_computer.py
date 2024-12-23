import streamlit as st

from game_data.board import Board
from openai_calls.speech2text import record_message
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually
from utils import print_ts


def do_computer_turn(board: Board):
    # TODO: we'll simplify things, the computer just shuffles a question
    trait_to_ask = board.get_non_trivial_trait()
    prompt = (
        f'''You are an AI playing a game of guess-who. You are trying to guess the hidden character of your opponent.
        You want to ask a yes or no question about whether the character has the following trait: {trait_to_ask}."''')
    print_ts(f"Planning to ask the user the following prompt: {prompt}")
    ai_question = ask_textually(prompt)
    st.info(f"AI Question: {ai_question}", icon="🤖")
    play_voice(ai_question)
    user_answer = record_message(key="user_answer")
    st.info(f"User Answer: {user_answer}", icon="👤")
    prompt = (f'''You are an AI playing a game of guess who. You asked a question about a trait, and your opponent answered. 
    You need to decide whether the answer means that the conditions is fulfilled.
    Your question was {ai_question} and the answer was {user_answer}.
    Please answer only YES or NO, without other information.''')
    ai_answer = ask_textually(prompt)
    print_ts(f"AI Answer: {ai_answer}")
    if len(ai_answer) > 10:
        raise ValueError(f"Oops! the answer is too long: {ai_answer}")
    if 'yes' in ai_answer.lower():
        has_traits = True
    elif 'no' in ai_answer.lower():
        has_traits = False
    else:
        raise ValueError(f"Oops! the answer is not YES or NO: {ai_answer}")
    board.update_board(traits=[trait_to_ask], has_traits=has_traits)