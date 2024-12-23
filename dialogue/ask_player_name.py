from dialogue.system_message import SYS_MSG
from game_data.game_state import GameState
from openai_calls.text2speech import play_voice
from openai_calls.text2text import ask_textually


def ask_player_name(gs: GameState):
    opening_prompt = (f"{SYS_MSG}. Welcome the kid to the game, and explain in one sentence what are the rules of "
                      f"Guess Who. End by asking the kid's name")
    ai_intro = ask_textually(opening_prompt)
    play_voice(ai_intro)
    gs.asked_name = True