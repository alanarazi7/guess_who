import random
from dataclasses import dataclass
from typing import Optional

import streamlit as st

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
from utils import print_ts, normalize_str



def ask_your_card(gs: GameState):
    secret_card_prompt = f'''The player's name is {gs.player_name}. Ask him to pick a character from game board in 
    front of him. Clarify that you'll just keep the secret identity in order to keep track on the game, and that you 
    won't use it to win him.'''
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


def choose_ai_card(gs: GameState):
    if not gs.ai_char:
        gs.ai_char = random.choice(CHARACTERS)


def do_player_turn(gs: GameState):
    traits = None
    for attempt in range(3):
        traits = user_to_ask_question(gs)
        if traits:
            break
        failure_prompt = f'''The kid name is {gs.player_name}. He asked a question but it was either 
        unclear, or invalid. Ask gently to ask again.'''
        tell_prompt(failure_prompt)

    if traits is None:
        st.error("Sorry, we couldn't understand your question, please try again.")
        return

    has_traits = gs.ai_char.has_traits(traits)
    assistant_answer = f"The answer to your question is: {has_traits}"
    st.info(f"AI Answer: {assistant_answer}", icon="🤖")
    play_voice(assistant_answer)
    gs.player_board.update_board(traits, has_traits)

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

def main():
    st.title("Guess Who ❓")
    display_board_image()
    gs = get_game_state()

    # Start the game when the button is clicked
    if not gs.start_game and st.button("Start Game!"):
        st.success("Starting the game!", icon="🎉")
        gs.start_game = True

    # Explain the game and ask for the player's name
    if gs.start_game and not gs.player_name:
        explain_game_and_ask_name(gs)

    # Greet the player after receiving their name and ask to pick their secret card
    if gs.player_name and not gs.player_char:
        st.success(f"Nice to meet you, {gs.player_name}!", icon="👋")
        ask_your_card(gs)

    # Confirm the player's chosen character and let the computer choose a character
    if gs.player_char and not gs.ai_char:
        choose_ai_card(gs)
        st.success(f"Great! The computer and player have both chosen their characters. Let's begin!", icon="🎮")

    if gs.ai_char:
        st.warning(f"Your character is {gs.player_char.name}. Don't forget it!", icon="👤")
        with st.expander("AI's Secret Character"):
            st.success(f"The AI has chosen: {gs.ai_char.name}", icon="🤖")

    if (not gs.ai_board) and (not gs.player_board):
        gs.player_board = Board(remaining=list(CHARACTERS))
        gs.ai_board = Board(remaining=list(CHARACTERS))

    if gs.ai_char and not gs.questions_asked:
        tell_prompt(f"Invite the player {gs.player_name} to ask his first question, which should be a yes/no one.")
        gs.questions_asked = True

    if not gs.questions_asked:
        return

    # while True:
    #     do_player_turn(gs)
    #     if len(gs.player_board.remaining) > 1:
    #         remaining = str([p.name for p in gs.player_board.remaining])
    #         st.info(f"{len(gs.player_board.remaining)} Remaining Characters: {remaining}", icon="👤")
    #         play_voice(f"You have {len(gs.player_board.remaining)} more possible characters!")
    #     else:
    #         winning_msg = f"You found my character! It is {gs.player_board.remaining[0].name}."
    #         st.success(winning_msg)
    #         play_voice(winning_msg)
    #         break
    #     break
    # do_computer_turn(ai_board)
    # if len(ai_board.remaining) > 1:
    #     st.info(f"{len(ai_board.remaining)} Remaining Characters: {str([p.name for p in ai_board.remaining])}", icon="🤖")
    #     play_voice(f"I have {len(ai_board.remaining)} more possible characters!")
    # else:
    #     winning_msg = f"AI: I have found your character! It is {ai_board.remaining[0].name}."
    #     st.success(winning_msg)
    #     play_voice(winning_msg)
    #     break

if __name__ == "__main__":
    main()
