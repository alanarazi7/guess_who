import random

import streamlit as st

from dialogue.ask_card import ask_your_card
from dialogue.introduction import explain_game_and_ask_name
from dialogue.turn_ai import get_ai_q, parse_player_answer_to_ai_q, reset_ai_turn_data, ai_won
from dialogue.turn_player import extract_traits_from_q, declare_invalid_q, update_after_player_q, user_won
from game_data.board import Board
from game_data.characters import CHARACTERS
from game_data.game_state import get_game_state
from game_data.image import display_board_image
from openai_calls.prompt2speech import tell_prompt
from openai_calls.speech2text import record_message
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually


def main():
    st.title("Guess Who ❓")
    gs = get_game_state()

    # if not gs.ai_char:
    #     display_board_image()
    #
    # if (not gs.start_game) and st.button("Start Game! 🎉"):
    #     gs.start_game = True
    #
    # if gs.start_game and not gs.player_name:
    #     explain_game_and_ask_name(gs)
    #
    # if gs.player_name and not gs.pick_character:
    #     st.success(f"Welcome {gs.player_name}! Let's have some fun!", icon="🎮")
    #     if st.button("Pick Your Character 🎭"):
    #         gs.pick_character = True
    #
    # if gs.pick_character and (not gs.player_char):
    #     ask_your_card(gs)
    #
    # if gs.player_char and not gs.ai_char:
    #     gs.ai_char = random.choice(CHARACTERS)
    #
    # if gs.ai_char:
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         st.image(gs.player_char.image, caption=f"Hi {gs.player_name}! Your secret character is {gs.player_char}! 👤")
    #     with col2:
    #         with st.expander("AI's Secret Character"):
    #             st.image(gs.ai_char.image, caption=f"AI's Secret Character is {gs.ai_char} 🤖")
    #     st.markdown("-----------------------------------------------------------")
    #
    # if not gs.ai_board or not gs.player_board:
    #     gs.player_board = Board(remaining=list(CHARACTERS))
    #     gs.ai_board = Board(remaining=list(CHARACTERS))

    gs.player_name = "Alan"
    gs.ai_char = CHARACTERS[0]
    gs.player_char = CHARACTERS[1]

    if gs.ai_char and (not gs.who_starts_was_asked):
        if st.button("Who starts? 1️⃣️"):
            gs.who_starts_was_asked = True

    if gs.who_starts_was_asked and (not gs.who_starts):
        q = (f"Remind the player {gs.player_name} that questions should be of Yes/No answer. Ask him who "
             f"should start the game (him or you).")
        tell_prompt(q)
        if st.button("Record Who Starts 🎤"):


        gs.who_starts = record_message(key="who_starts")
        st.rerun()

    if gs.who_starts and (not gs.questions_asked):
        prompt = (f"You asked the player to decide who starts the game, and he said: {gs.who_starts}."
                  f"If he said `I start`, then the player should start. If he said `You start`, then the AI "
                  f"should start. Return a JSON with the key `player_start` and the value being a boolean.")
        who_starts_answer = ask_textually(prompt, force_json=True)
        is_player_start = who_starts_answer['player_start']
        if isinstance(is_player_start, bool):
            gs.player_turn = is_player_start
            gs.ai_turn = not is_player_start
        else:
            st.error("Invalid response. Please try again.")
        gs.questions_asked = True

    if not gs.questions_asked:
        return

    if gs.player_turn:
        gs.player_q = record_message(key="user_question")
        if gs.player_q:
            traits = extract_traits_from_q(gs)
            if not traits:
                return declare_invalid_q(gs)
            update_after_player_q(gs, traits)
            if len(gs.player_board.remaining) > 1:
                st.info(gs.player_board.remaining_msg, icon="👤")
            else:
                user_won(gs)
            gs.player_turn = False
            gs.last_turn_was_human = True

    if gs.last_turn_was_human and (not gs.player_turn) and (not gs.ai_turn) and st.button("Next Turn 🤖"):
        gs.ai_turn = True

    if gs.ai_turn:
        if not gs.ai_trait:
            get_ai_q(gs)
        if gs.ai_q:
            play_voice(gs.ai_q)
            gs.ai_q_user_answer = record_message(key="user_answer")
        if gs.ai_q_user_answer:
            parse_player_answer_to_ai_q(gs)
            reset_ai_turn_data(gs)
            if len(gs.ai_board.remaining) > 1:
                st.info(gs.ai_board.remaining_msg, icon="🤖")
            else:
                ai_won(gs)

    if (not gs.last_turn_was_human) and (not gs.ai_turn) and (not gs.player_turn) and st.button("Next Turn 👤"):
        gs.player_turn = True

    if gs.game_over:
        st.warning("The game is over. Please refresh the page to play again.", icon="🏁")

if __name__ == "__main__":
    main()
