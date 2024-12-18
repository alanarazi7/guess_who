import streamlit as st
from PIL import Image

from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually

# Predefined characters
characters = [
    {"name": "Alex", "gender": "Male"},
    {"name": "Taylor", "gender": "Female"},
    {"name": "Jordan", "gender": "Male"},
    {"name": "Morgan", "gender": "Female"},
    {"name": "Casey", "gender": "Male"}
]


def main():
    st.title("AI-Powered Guess Who Game 🎤")

    # Load and display the image
    image_path = "pictures/guess_who_board.jpg"
    image = Image.open(image_path)
    st.image(image, caption="Guess Who Board", use_column_width=True)

    st.write("**Think of a character from the list below, and I will try to guess it!**")
    st.write("### Characters:")
    for i, char in enumerate(characters):
        st.write(f"{i + 1}. Name: {char['name']}, Gender: {char['gender']}")

    # Start Game
    st.write("\n---")
    st.write("🎙️ **Step 1: I will ask a question. Speak your answer!**")
    if st.button("Start Game!"):
        play_voice(
            "Welcome to the AI-Powered Guess Who Game! Think of a character from the list, and I will try to guess it.")

        # Turn 1: First Question
        aio_question_1 = "Is your character male or female?"
        play_voice(aio_question_1)
        st.write(f"AI: {aio_question_1}")
        st.info("Listening for your answer...")
        user_answer_1 = do_speech_to_text()
        st.success(f"You said: {user_answer_1}")

        # Turn 2: Generate Second Question
        ai_prompt_2 = f"The user said their character is {user_answer_1}. Ask a second question to guess their character."
        ai_question_2 = ask_textually(ai_prompt_2)
        play_voice(ai_question_2)
        st.write(f"AI: {ai_question_2}")
        st.info("Listening for your next answer...")
        user_answer_2 = do_speech_to_text()
        st.success(f"You said: {user_answer_2}")

        # Final Guess
        ai_prompt_guess = f"Based on the answers: 1) {user_answer_1}, 2) {user_answer_2}, guess the character from the following list: {characters}."
        ai_guess = ask_textually(ai_prompt_guess)
        play_voice(f"I guess your character is {ai_guess}!")
        st.success(f"🎉 AI Guess: {ai_guess}")


if __name__ == "__main__":
    main()
