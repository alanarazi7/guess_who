from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually


def tell_prompt(prompt: str):
    response = ask_textually(prompt)
    play_voice(response)