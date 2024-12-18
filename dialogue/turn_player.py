import streamlit as st

from dialogue.question_to_condition import get_trait_from_question
from game_data.board import Board
from game_data.characters import Person
from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
from utils import print_ts


def do_player_turn(assistant_hidden_char: Person, board: Board):
    user_question = do_speech_to_text()
    st.info(f"User Question: {user_question}", icon="👤")
    traits = get_trait_from_question(user_question)
    gender_traits = {'male', 'female'}
    if len(traits) > 1 and set(traits).union(gender_traits):
        traits = list(set(traits).difference(gender_traits))
        print_ts(f"Removing the gender traits, got now {traits}")
    st.info(f"We looked at the following: {assistant_hidden_char.get_traits(traits)}", icon="🐛")
    if not traits:
        play_voice(f"I'm sorry, your question is not valid. I'm ending the game for now, but we'll fix this!")
        assert False
    has_traits = assistant_hidden_char.has_traits(traits)
    print_ts(f"We have determined that the answer to the question is: {has_traits}")
    assistant_answer = f"The answer to your question is: {has_traits}"
    st.info(f"AI Answer: {assistant_answer}", icon="🤖")
    play_voice(assistant_answer)
    board.update_board(traits, has_traits)
