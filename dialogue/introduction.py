from game_data.game_state import GameState
from openai_calls.prompt2speech import tell_prompt
from openai_calls.speech2text import record_message
from openai_calls.text2text import ask_textually


def explain_game_and_ask_name(gs: GameState):
    opening_prompt = f'''Welcome the kid to the game, and explain in one sentence what are the rules of Guess Who. 
    End by asking the kid's name.'''

    if not gs.ai_intro:
        tell_prompt(opening_prompt)
        gs.ai_intro = True

    if not gs.player_name:
        player_name = record_message(key="player_name")
        if player_name:
            name_recognition_prompt = f'''You asked for a kid's name, and he said it's: {player_name}.
            Confirm the name. Output a JSON with the key `name` and the value being the name'''
            ai_name_recognition = ask_textually(name_recognition_prompt, force_json=True)
            gs.player_name = ai_name_recognition['name']