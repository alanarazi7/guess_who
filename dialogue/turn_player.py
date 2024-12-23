# import streamlit as st
#
# from dialogue.question_to_condition import get_trait_from_question
# from game_data.board import Board
# from game_data.characters import Person
# from openai_calls.speech2text import record_message
# from openai_calls.text2speech import play_voice
# from openai_calls.text2text import ask_textually
# from utils import print_ts
#
#
# def do_player_turn(assistant_hidden_char: Person, board: Board, player_name: str):
#     traits = None
#     for attempt in range(3):
#         traits = user_to_ask_question(assistant_hidden_char)
#         if traits:
#             break
#         print_ts(f"Attempt {attempt + 1} failed, retrying. Got {traits}")
#         failure_prompt = f"""{SYS_MSG}. The kid name is {player_name}. He asked a question but it was either unclear,
#         or invalid. Ask it gently to ask again"""
#         failure_msg = ask_textually(failure_prompt)
#         play_voice(failure_msg)
#
#     if traits is None:
#         raise st.error("Sorry, we couldn't understand your question, please try again.")
#
#     has_traits = assistant_hidden_char.has_traits(traits)
#     print_ts(f"We have determined that the answer to the question is: {has_traits}")
#     assistant_answer = f"The answer to your question is: {has_traits}"
#     st.info(f"AI Answer: {assistant_answer}", icon="🤖")
#     play_voice(assistant_answer)
#     board.update_board(traits, has_traits)
#
#
# def user_to_ask_question(assistant_hidden_char: Person):
#     user_question = record_message(key="user_question")
#     st.info(f"User Question: {user_question}", icon="👤")
#     traits = get_trait_from_question(user_question)
#     gender_traits = {'male', 'female'}
#     if len(traits) > 1 and set(traits).union(gender_traits):
#         traits = list(set(traits).difference(gender_traits))
#         print_ts(f"Removing the gender traits, got now {traits}")
#     st.info(f"We looked at the following: {assistant_hidden_char.get_traits(traits)}", icon="🐛")
#     return traits