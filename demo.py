import random
from dataclasses import dataclass

import streamlit as st

from dialogue.ask_your_card import ask_your_card
from dialogue.introduction import explain_game_and_ask_name
from dialogue.system_message import SYS_MSG
from dialogue.turn_player import do_player_turn

from dialogue.turn_computer import do_computer_turn
from game_data.board import Board
from game_data.characters import CHARACTERS
from game_data.game_state import GameState, get_game_state, start_game
from game_data.image import display_board_image
from openai_calls.speech2text import record_message
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually
from utils import print_ts



def main():
    st.title("Guess Who ❓")
    display_board_image()
    gs = get_game_state()

    if not gs.start_game:
        start_game(gs)

    if gs.start_game and not gs.player_name:
        explain_game_and_ask_name(gs)

    if gs.player_name:
        st.success(f"Nice to meet you, {gs.player_name}!", icon="👋")
        st.warning("Implement next step!")
    #
    # # Step 2: Process the recorded name
    # if game_state.waiting_for_name and not game_state.player_name:
    #     player_name = record_message(key="player_name")
    #     if player_name:  # Only proceed if something was recorded
    #         name_recognition_prompt = (f"You asked for a kid's name, and he said it's: {player_name}."
    #                                    f"Confirm the name. Output a JSON with the key `name` and the value being the name")
    #         ai_name_recognition = ask_textually(name_recognition_prompt, force_json=True)
    #         game_state.player_name = ai_name_recognition['name']
    #         game_state.waiting_for_name = False
    #
    # # Step 3: Greet the player once the name is recorded
    # if game_state.player_name:
    #     st.success(f"Nice to meet you, {game_state.player_name}!", icon="👋")


    # user_name = explain_game_and_ask_name()
    # assistant_hidden_char = random.choice(CHARACTERS)
    # player_hidden_char = ask_your_card(user_name=user_name)
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
