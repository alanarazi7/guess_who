import streamlit as st

from game_data.game_state import GameState
from openai_calls.prompt2speech import tell_prompt
from openai_calls.text2text import ask_textually


def get_ai_q(gs: GameState) -> str:
    gs.ai_trait = gs.ai_board.get_non_trivial_trait()
    prompt = (
        f"""You are an AI playing a game of Guess Who. You are trying to guess the hidden character of your opponent.\n
        You want to ask a yes or no question about whether the character has the following trait: {gs.ai_trait}."""
    )
    gs.ai_q = ask_textually(prompt)


def parse_player_answer_to_ai_q(gs: GameState):
    assert gs.ai_q and gs.ai_q_user_answer
    prompt = (
        f"""You are an AI playing a game of Guess Who. You asked a question about a trait, and your opponent answered.\n
        You need to decide whether the answer means the condition is fulfilled.\n
        Your question was `{gs.ai_q}` and the answer was `{gs.ai_q_user_answer}`.\n
        Please answer only YES or NO, without other information."""
    )
    ai_answer = ask_textually(prompt)
    if len(ai_answer) > 10:
        raise ValueError(f"Oops! the answer is too long: {ai_answer}")
    if 'yes' in ai_answer.lower():
        has_traits = True
    elif 'no' in ai_answer.lower():
        has_traits = False
    else:
        raise ValueError(f"Oops! the answer is not YES or NO: {ai_answer}")
    gs.ai_board.update_board(traits=[gs.ai_trait], has_traits=has_traits)


def reset_ai_turn_data(gs: GameState):
    gs.ai_trait = None
    gs.ai_q_user_answer = None
    gs.ai_q = None
    gs.ai_turn = False
    gs.last_turn_was_human = False

def ai_won(gs: GameState):
    player_char = gs.ai_board.remaining[0].name
    tell_prompt(f"Tell the player {gs.player_name} that you found his character, and it's {player_char}")
    st.success(f"AI found your character! It is {player_char}.", icon="🤖")
    gs.game_over = True