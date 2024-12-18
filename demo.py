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

# Start the game
play_voice("Welcome to the AI-Powered Guess Who Game! Think of a character from the list, and I will try to guess it.")

# Turn 1: Ask the first question
aio_question_1 = "Is your character male or female?"
play_voice(aio_question_1)
user_answer_1 = do_speech_to_text()

# Turn 2: Generate second question based on the answer
ai_prompt_2 = f"The user said their character is {user_answer_1}. Ask a second question to guess their character."
ai_question_2 = ask_textually(ai_prompt_2)
play_voice(ai_question_2)
user_answer_2 = do_speech_to_text()

# Final Guess: Generate guess based on answers
ai_prompt_guess = f"Based on the answers: 1) {user_answer_1}, 2) {user_answer_2}, guess the character from the following list: {characters}."
ai_guess = ask_textually(ai_prompt_guess)
play_voice(f"I guess your character is {ai_guess}!")