import random

import streamlit as st
from PIL import Image

from dialogue.ask_your_card import ask_your_card
from dialogue.introduction import explain_game_and_ask_name
from dialogue.turn_player import do_player_turn

from dialogue.turn_computer import do_computer_turn
from game_data.board import Board
from game_data.characters import CHARACTERS
from openai_calls.text2speech import play_voice
from utils import print_ts


def main():
    st.title("AI-Powered Guess Who Game 🎤")

    # Load and display the image
    image_path = "pictures/guess_who_board.jpg"
    image = Image.open(image_path)
    st.image(image, caption="Guess Who Board")

    st.write("**Think of a character from the picture above, and I will try to guess it!**")

    if st.button("Start Game!"):
        user_name = explain_game_and_ask_name()
        assistant_hidden_char = random.choice(CHARACTERS)
        player_hidden_char = ask_your_card(user_name=user_name)
        # let's display his choice
        st.info(f"I chosen {assistant_hidden_char}. Try to guess who it is", icon="🤖")
        st.info(f"You picked {player_hidden_char}, but don't worry, I won't cheat!", icon="🤫")
        # Start Game
        # TODO: randomly decide who starts...
        st.write("\n---")
        print_ts("Starting the game!")

        player_board = Board(remaining=list(CHARACTERS))
        ai_board = Board(remaining=list(CHARACTERS))
        while True:
            play_voice("Please ask a question.")
            do_player_turn(assistant_hidden_char=assistant_hidden_char, board=player_board, player_name=user_name)
            if len(player_board) > 1:
                st.info(f"{len(player_board)} Remaining Characters: {str([p.name for p in player_board.remaining])}", icon="👤")
                play_voice(f"You have {len(player_board)} more possible characters!")
            else:
                winning_msg = f"You found my character! It is {player_board.remaining[0].name}."
                st.success(winning_msg)
                play_voice(winning_msg)
                break
            do_computer_turn(ai_board)
            if len(ai_board) > 1:
                st.info(f"{len(ai_board)} Remaining Characters: {str([p.name for p in ai_board.remaining])}", icon="🤖")
                play_voice(f"I have {len(ai_board)} more possible characters!")
            else:
                winning_msg = f"AI: I have found your character! It is {ai_board.remaining[0].name}."
                st.success(winning_msg)
                play_voice(winning_msg)
                break

if __name__ == "__main__":
    main()
