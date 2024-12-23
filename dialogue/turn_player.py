from typing import List

import streamlit as st

from dialogue.question_to_condition import get_trait_from_question
from game_data.game_state import GameState
from openai_calls.constants import DEBUG_MODE
from openai_calls.prompt2speech import tell_prompt


def update_after_player_q(gs: GameState, traits: List[str]):
    has_traits = gs.ai_char.has_traits(traits)
    prompt = f"Paraphrase to an engaging full sentence answer:\n\nQ: {gs.player_q}\n\nA: {has_traits}."
    tell_prompt(prompt)
    gs.player_board.update_board(traits, has_traits)
    gs.player_q_attempts = 0

def declare_invalid_q(gs: GameState):
    failure_prompt = f'''The kid name is {gs.player_name}. He asked a question but it was either 
    unclear, or invalid. Ask gently to ask again.'''
    tell_prompt(failure_prompt)
    gs.player_q = None


def extract_traits_from_q(gs: GameState) -> List[str]:
    gs.player_q_attempts += 1
    traits = get_trait_from_question(gs.player_q)
    gender_traits = {'male', 'female'}
    if len(traits) > 1 and set(traits).union(gender_traits):
        traits = list(set(traits).difference(gender_traits))
    if DEBUG_MODE:
        st.info(f"We looked at the following: {gs.ai_char.get_traits(traits)}", icon="🐛")
    return traits


def user_won(gs: GameState):
    winning_msg = f"You found my character! It is {gs.player_board.remaining[0].name}."
    st.success(winning_msg)
    tell_prompt(f"Tell the player that he guessed the character: {gs.player_board.remaining[0].name}.")
    gs.game_over = True