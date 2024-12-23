import random

import streamlit as st

from dialogue.ask_card import ask_your_card
from dialogue.introduction import explain_game_and_ask_name
from dialogue.question_to_condition import get_trait_from_question
from game_data.board import Board
from game_data.characters import CHARACTERS, Person
from game_data.game_state import GameState, get_game_state
from game_data.image import display_board_image
from openai_calls.constants import DEBUG_MODE
from openai_calls.prompt2speech import tell_prompt
from openai_calls.speech2text import record_message
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually
from utils import print_ts


def user_to_ask_question(gs: GameState):
    user_question = record_message(key="user_question")
    st.info(f"User Question: {user_question}", icon="👤")
    traits = get_trait_from_question(user_question)
    gender_traits = {'male', 'female'}
    if len(traits) > 1 and set(traits).union(gender_traits):
        traits = list(set(traits).difference(gender_traits))
        print_ts(f"Removing the gender traits, got now {traits}")
    if DEBUG_MODE:
        st.info(f"We looked at the following: {gs.ai_char.get_traits(traits)}", icon="🐛")
    return traits

def do_computer_turn(gs: GameState):
    trait_to_ask = gs.ai_board.get_non_trivial_trait()
    prompt = (
        f"""You are an AI playing a game of Guess Who. You are trying to guess the hidden character of your opponent.\n
        You want to ask a yes or no question about whether the character has the following trait: {trait_to_ask}."""
    )
    print_ts(f"Planning to ask the user the following prompt: {prompt}")
    ai_question = ask_textually(prompt)
    st.info(f"AI Question: {ai_question}", icon="🤖")
    play_voice(ai_question)
    user_answer = record_message(key="user_answer")
    st.info(f"User Answer: {user_answer}", icon="👤")
    prompt = (
        f"""You are an AI playing a game of Guess Who. You asked a question about a trait, and your opponent answered.\n
        You need to decide whether the answer means the condition is fulfilled.\n
        Your question was {ai_question} and the answer was {user_answer}.\n
        Please answer only YES or NO, without other information."""
    )
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
    gs.ai_board.update_board(traits=[trait_to_ask], has_traits=has_traits)


def main():
    st.title("Guess Who ❓")
    display_board_image()
    gs = get_game_state()

    if (not gs.start_game) and st.button("Start Game! 🎉"):
        gs.start_game = True

    if gs.start_game and not gs.player_name:
        explain_game_and_ask_name(gs)

    if gs.player_name and not gs.pick_character:
        st.success(f"Welcome {gs.player_name}! Let's have some fun!", icon="🎮")
        if st.button("Pick Your Character 🎭"):
            gs.pick_character = True

    if gs.pick_character and (not gs.player_char):
        ask_your_card(gs)

    gs.player_char = CHARACTERS[0]
    gs.player_name = "Alan"

    if gs.player_char and not gs.ai_char:
        gs.ai_char = random.choice(CHARACTERS)

    if gs.ai_char:
        st.warning(f"Hi {gs.player_name}! Your character is {gs.player_char.name}. Don't forget it!", icon="👤")
        with st.expander("AI's Secret Character"):
            st.info(f"The AI has chosen: {gs.ai_char.name}", icon="🤖")
        st.markdown("-----------------------------------------------------------")

    if not gs.ai_board or not gs.player_board:
        gs.player_board = Board(remaining=list(CHARACTERS))
        gs.ai_board = Board(remaining=list(CHARACTERS))

    if gs.ai_char and (not gs.questions_asked):
        if st.button("Ask Question ▶️"):
            q = f"Tell {gs.player_name} to ask his first question, which should be a yes/no one."
            tell_prompt(q)
            gs.questions_asked = True

    if not gs.questions_asked:
        return

    if gs.player_turn:
        gs.player_q = record_message(key="user_question")
        if gs.player_q:
            gs.player_q_attempts += 1
            traits = get_trait_from_question(gs.player_q)
            gender_traits = {'male', 'female'}
            if len(traits) > 1 and set(traits).union(gender_traits):
                traits = list(set(traits).difference(gender_traits))
            if DEBUG_MODE:
                st.info(f"We looked at the following: {gs.ai_char.get_traits(traits)}", icon="🐛")
            if not traits:
                failure_prompt = f'''The kid name is {gs.player_name}. He asked a question but it was either 
                unclear, or invalid. Ask gently to ask again.'''
                tell_prompt(failure_prompt)
            else:
                has_traits = gs.ai_char.has_traits(traits)
                prompt = f"Paraphrase to an engaging full sentence answer:\n\nQ: {gs.player_q}\n\nA: {has_traits}."
                tell_prompt(prompt)
                gs.player_board.update_board(traits, has_traits)
                gs.player_q_attempts = 0
            gs.player_q = None
            if len(gs.player_board.remaining) > 1:
                st.info(gs.player_board.remaining_msg, icon="👤")
            else:
                winning_msg = f"You found my character! It is {gs.player_board.remaining[0].name}."
                st.success(winning_msg)
                tell_prompt(f"Tell the player that he guessed the character: {gs.player_board.remaining[0].name}.")
                gs.game_over = True
            gs.player_turn = False
            if st.button("Next Turn 🤖"):
                gs.ai_turn = True
    if gs.ai_turn:
        st.warning("AI's Turn! 🤖")
    #    do_computer_turn(gs)
    #     if len(gs.ai_board.remaining) > 1:
    #         st.info(gs.ai_board.remaining_msg, icon="🤖")
    #         play_voice(f"I have {len(gs.ai_board.remaining)} more possible characters!")
    #     else:
    #         winning_msg = f"AI: I have found your character! It is {gs.ai_board.remaining[0].name}."
    #         st.success(winning_msg)
    #         play_voice(winning_msg)
    #         gs.game_over = True

    if gs.game_over:
        st.warning("The game is over. Please refresh the page to play again.", icon="🏁")

if __name__ == "__main__":
    main()
