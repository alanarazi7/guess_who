from dialogue.system_message import SYS_MSG
from game_data.characters import Person, CHARACTERS
from openai_calls.speech2text import do_speech_to_text
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually


def ask_your_card(user_name) -> Person:
    secret_card_prompt = (f"{SYS_MSG}. The kid's name is {user_name}. "
                          f"Ask him/her to pick a character and tell it to you."
                          f"Clarify that although he's telling it to you, you'll keep it a secret and only will use it to "
                          f"keep track of the game - be fun about it!")
    ai_funny = ask_textually(secret_card_prompt)
    play_voice(ai_funny)
    user_choice = do_speech_to_text()
    understanding_name_prompt = (f"{SYS_MSG}. The possible names are {[p.name for p in CHARACTERS]}."
                                 f"You asked the kid to pick a character and tell it to you. He said: {user_choice}."
                                 f"Confirm the name of the picked character. Output a JSON with the key `name` and the value being the name")
    ai_understanding_name = ask_textually(understanding_name_prompt)
    play_voice(f"Got it, you picked {ai_understanding_name}!")
    character = [p for p in CHARACTERS if p.name == ai_understanding_name.lower().replace(".", '').strip()][0]
    return character