import random

import streamlit as st
from PIL import Image

from constants import IS_FULL_DEMO
from dialogue.introduction import explain_game_and_ask_name
from dialogue.turn_player import do_player_turn

from dialogue.turn_computer import do_computer_turn
from game_data.characters import CHARACTERS, characters_to_dataframe
from openai_calls.text2speech import play_voice
from utils import print_ts


def main():
    st.title("AI-Powered Guess Who Game 🎤")

    # Load and display the image
    image_path = "pictures/guess_who_board.jpg"
    image = Image.open(image_path)
    st.image(image, caption="Guess Who Board")

    st.write("**Think of a character from the list below, and I will try to guess it!**")
    st.write("### Characters:")

    # Display characters in a dataframe with emojis
    df = characters_to_dataframe(CHARACTERS)
    st.table(df)

    if st.button("Start Game!"):
        if IS_FULL_DEMO:
            explain_game_and_ask_name()
        # TODO: here we need to hide the chosen character - for debug purpose, we want to show it
        assistant_hidden_char = random.choice(CHARACTERS)
        # let's display his choice
        st.info(f"AI: I have chosen a character: {assistant_hidden_char}. Try to guess who it is!")

        # Start Game
        # TODO: randomly decide who starts...
        st.write("\n---")
        print_ts("Starting the game!")

        remaining = list(CHARACTERS)
        for i in range(5):
            play_voice("Please ask a question.")
            do_player_turn(assistant_hidden_char=assistant_hidden_char)
            print_ts(f"Still have {len(remaining)} remaining characters.")
            possible_characters = do_computer_turn(CHARACTERS)
            print_ts(f"There are now {len(possible_characters)} possible characters.")
            possible_names = {n.lower() for n in possible_characters}
            remaining = [p for p in remaining if p.name.lower() in possible_names]
            assert len(remaining) == len(possible_characters), f"{remaining=}, {possible_characters=}"
            st.info(f"{len(remaining)} Remaining Characters: {[p.name for p in remaining]}", icon="🤖")
            play_voice(f"I have {len(remaining)} more possible characters!")
        assert False

if __name__ == "__main__":
    main()
