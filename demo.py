import random
from dataclasses import asdict

import pandas as pd
import streamlit as st
from PIL import Image

from constants import IS_FULL_DEMO
from dialogue.introduction import explain_game_and_ask_name
from game_data.characters import CHARACTERS, characters_to_dataframe
from game_data.player_turn import PlayerTurn
from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually

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
    st.dataframe(df)

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
        play_voice("Let's get started! Please ask a question.")

        # Initial dataframe for filtering
        current_df = pd.DataFrame(CHARACTERS)


        ### user asks a question
        user_question = do_speech_to_text()
        prompt = (f"You are an AI assistant playing guess-who, and your character is {asdict(assistant_hidden_char)}."
                  f"The user has asked you: {user_question}. You should reason about whether the answer is."
                  f"After your finish reasoning, output the following format - FINAL_ANSWER: Yes/No")
        st.write(f"Planning to ask the AI the following prompt: {prompt}")
        ai_answer = ask_textually(prompt)
        st.write(f"AI Answer: {ai_answer}")
        last_word = ai_answer.split()[-1].lower()
        if last_word not in ["yes", "no"]:
            raise ValueError(f"AI answer must be 'Yes' or 'No', but it answered: {ai_answer}")
        play_voice(f"The answer to your question is: {last_word}")


        ## computer asks a question
        the_board = current_df.to_dict('records')
        prompt = (f"You are an AI playing a game of guess-who. You are trying to guess the hidden character of your opponent. So far, the remaining characters in the board are the following ones:"
                  f"{the_board}. You have to ask a question to the user to try to guess the character, and it should be a yes/no question. What is your question?")
        st.write(f"Planning to ask the user the following prompt: {prompt}")
        ai_question = ask_textually(prompt)
        st.write(f"AI Question: {ai_question}")
        play_voice(ai_question)
        user_answer = do_speech_to_text()
        prompt = (f"You are an AI playing a game of guess who. This is the board you have right now: {the_board}."
                  f"You asked the user the following question: {ai_question}. The user answered: {user_answer}."
                  f"We now want to filter all the characters that are still possible given the user's answer. "
                  f"What are the characters that are still possible?"
                  f"Answer in a dictionary, where the keys are the character names, and each dictionary has two keys: reasoning and is_possible, where this should be a boolean."
                  f"Make sure you provide a final answer about each of the characters.")
        st.write(f"Planning to ask the AI the following prompt: {prompt}")
        ai_answer = ask_textually(prompt)
        st.write(f"AI Answer: {ai_answer}")
        assert False, "yalla"






        # First Turn
        def filter_gender(df, answer):
            return df[df['gender'].str.lower() == answer.lower()]

        turn_1 = PlayerTurn(question="Is your character male or female?", filter_function=filter_gender)
        turn_1.ask_question()
        turn_1.filter_rows(current_df)
        turn_1.update_game()

        # Update dataframe for next turn
        current_df = turn_1.updated_df

        # Second Turn
        def filter_hair_color(df, answer):
            return df[df['hair_color'].str.lower() == answer.lower()]

        ai_prompt_2 = f"The user said their character is {turn_1.answer}. Ask a second question to guess their character."
        question_2 = ask_textually(ai_prompt_2)
        turn_2 = PlayerTurn(question=question_2, filter_function=filter_hair_color)
        turn_2.ask_question()
        turn_2.filter_rows(current_df)
        turn_2.update_game()

        # Final Guess
        ai_prompt_guess = f"Based on the answers: 1) {turn_1.answer}, 2) {turn_2.answer}, guess the character from the following list: {current_df.to_dict('records')}"
        ai_guess = ask_textually(ai_prompt_guess)
        play_voice(f"I guess your character is {ai_guess}!")
        st.success(f"🎉 AI Guess: {ai_guess}")

if __name__ == "__main__":
    main()
