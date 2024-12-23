import random
from dataclasses import dataclass
from typing import Optional

import streamlit as st

from dialogue.system_message import SYS_MSG
from dialogue.turn_player import do_player_turn

from dialogue.turn_computer import do_computer_turn
from game_data.board import Board
from game_data.characters import CHARACTERS, Person
from game_data.image import display_board_image
from openai_calls.speech2text import record_message
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually
from utils import print_ts, normalize_str


@dataclass
class GameState:
    start_game: bool = False
    ai_intro: Optional[str] = None
    player_name: Optional[str] = None
    player_hidden_char: Optional[Person] = None


def get_game_state() -> GameState:
    if "game_state" not in st.session_state:
        st.session_state.game_state = GameState()
    return st.session_state.game_state


def start_game(gs: GameState):
    if st.button("Start Game!"):
        st.info("Starting the game!", icon="🎉")
        gs.start_game = True


def explain_game_and_ask_name(gs: GameState):
    opening_prompt = (f"{SYS_MSG}. Welcome the kid to the game, and explain in one sentence what are the rules of "
                      f"Guess Who. End by asking the kid's name")

    # Generate AI introduction once
    if not gs.ai_intro:
        gs.ai_intro = ask_textually(opening_prompt)
        play_voice(gs.ai_intro)

    # Record player's name if not already done
    if not gs.player_name:
        player_name = record_message(key="player_name")
        if player_name:
            name_recognition_prompt = (f"You asked for a kid's name, and he said it's: {player_name}."
                                       f"Confirm the name. Output a JSON with the key `name` and the value being the name")
            ai_name_recognition = ask_textually(name_recognition_prompt, force_json=True)
            gs.player_name = ai_name_recognition['name']


def ask_your_card(gs: GameState):
    if not gs.player_hidden_char:
        secret_card_prompt = (f"{SYS_MSG}. The kid's name is {gs.player_name}. "
                              f"Ask him/her to pick a character from the options on the game board in front of him. "
                              f"Clarify that although he's telling it to you, you'll keep it a secret and only will use it to "
                              f"keep track of the game - be fun about it!")
        ai_funny = ask_textually(secret_card_prompt)
        play_voice(ai_funny)

        user_choice = record_message(key="user_choice")
        if user_choice:
            print_ts(f"The user chose: {user_choice}")
            understanding_name_prompt = (f"{SYS_MSG}. The possible names are {[p.name for p in CHARACTERS]}. "
                                         f"You asked the kid to pick a character and tell it to you. He said: {user_choice}. "
                                         f"Confirm the name of the picked character. Output a JSON with the key `name` and the value being the name")
            ai_understanding_name = ask_textually(understanding_name_prompt, force_json=True)
            print_ts(f"Tried to parse, the user chose: {ai_understanding_name}")

            candidates = [p for p in CHARACTERS if
                          normalize_str(p.name) == normalize_str(ai_understanding_name['name'])]
            if len(candidates) == 1:
                gs.player_hidden_char = candidates[0]
            else:
                st.error("Oops! The character name could not be uniquely identified. Please try again.", icon="⚠")


def main():
    st.title("Guess Who ❓")
    display_board_image()
    gs = get_game_state()

    # Start the game when the button is clicked
    if not gs.start_game:
        start_game(gs)

    # Explain the game and ask for the player's name
    if gs.start_game and not gs.player_name:
        explain_game_and_ask_name(gs)

    # Greet the player after receiving their name
    if gs.player_name:
        st.success(f"Nice to meet you, {gs.player_name}!", icon="👋")

    # Ask the player to pick their secret card
    if gs.player_name and not gs.player_hidden_char:
        ask_your_card(gs)

    # Confirm the chosen character
    if gs.player_hidden_char:
        st.info(f"Great! You've picked {gs.player_hidden_char.name} as your secret character!", icon="😉")

    # player_hidden_char = ask_your_card(gs)

    # assistant_hidden_char = random.choice(CHARACTERS)

    # # let's display his choice
    # st.info(f"I chosen {assistant_hidden_char}. Try to guess who it is", icon="🤖")
    # st.info(f"You picked {player_hidden_char}, but don't worry, I won't cheat!", icon="🤫")
    # # Start Game
    # # TODO: randomly decide who starts...
    # st.write("\n---")
    # print_ts("Starting the game!")
    #
    # player_board = Board(remaining=list(CHARACTERS))
    # ai_board = Board(remaining=list(CHARACTERS))
    # while True:
    #     play_voice("Please ask a question.")
    #     do_player_turn(assistant_hidden_char=assistant_hidden_char, board=player_board, player_name=user_name)
    #     if len(player_board) > 1:
    #         st.info(f"{len(player_board)} Remaining Characters: {str([p.name for p in player_board.remaining])}", icon="👤")
    #         play_voice(f"You have {len(player_board)} more possible characters!")
    #     else:
    #         winning_msg = f"You found my character! It is {player_board.remaining[0].name}."
    #         st.success(winning_msg)
    #         play_voice(winning_msg)
    #         break
    #     do_computer_turn(ai_board)
    #     if len(ai_board) > 1:
    #         st.info(f"{len(ai_board)} Remaining Characters: {str([p.name for p in ai_board.remaining])}", icon="🤖")
    #         play_voice(f"I have {len(ai_board)} more possible characters!")
    #     else:
    #         winning_msg = f"AI: I have found your character! It is {ai_board.remaining[0].name}."
    #         st.success(winning_msg)
    #         play_voice(winning_msg)
    #         break

if __name__ == "__main__":
    main()
