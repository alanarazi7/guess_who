from dataclasses import asdict

import streamlit as st

from game_data.characters import Person
from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually
from utils import print_ts


def do_player_turn(assistant_hidden_char: Person):
    user_question = do_speech_to_text()
    st.info(f"User Question: {user_question}", icon="👤")
    prompt = (f"You are an AI assistant playing guess-who, and your character is {asdict(assistant_hidden_char)}."
              f"The user has asked you: {user_question}. Answer directly YES or NO, without chit-chat.")
    print_ts(f"Planning to ask the AI the following prompt: {prompt}")
    ai_answer = ask_textually(prompt)
    print_ts(f"AI Answer: {ai_answer}")
    last_word = ai_answer.split()[-1].lower().replace('.', "")
    if last_word not in ["yes", "no"]:
        raise ValueError(f"AI answer must be 'Yes' or 'No', but it answered: {ai_answer}")
    assistant_answer = f"The answer to your question is: {last_word}"
    st.info(f"AI Answer: {assistant_answer}", icon="🤖")
    play_voice(assistant_answer)