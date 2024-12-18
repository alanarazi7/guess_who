from game_data.characters import TRAITS
from openai_calls.text2text import ask_textually

template = """Consider that we are playing the game of "Guess Who", and that a character has the following set of traits {traits}.
The user now asked a question that should be mapped to one (or more) of the columns. 
You should map the question to the column and also say if the question is a positive or negative question. 
In order to be positive, at least one of the column should be positive.
In order to be negative, all the traits should be negative.
The output should be in JSON mode. Here are a few examples:

Question:
Is your character a boy?
Answer:
{'column': ['male'], 'positive': True}

Question:
Is this person wearing any accessories on their face or head?
Answer:
{'column': ['glasses', 'earrings', 'hat'], 'positive': True}

Question:
Does your character see well?
Answer:
{'column': ['glasses'], 'positive': False}

Question:
Does it have bright eyes?
Answer:
{'column': ['blue_eyes', 'green_eyes'], 'positive': True}

Question:
Does your character has a huge nose?
Answer:
{{'column': ['large_nose'], 'positive': True}}

Question:
{{question}}
Answer:
"""


def get_trait_from_question(question: str):
    prompt = template.replace('{traits}', str(TRAITS)).replace('{question}', question)
    answer = ask_textually(prompt, force_json=True)
    if not set(answer) == (expected_keys := {'column', 'positive'}):
        raise KeyError(f"Oops! expected {expected_keys} but got {answer}")
    col = answer['column']
    is_positive = answer['positive']
    return col, is_positive



if __name__ == '__main__':
    questions = [
        "Does this person have facial hair?",
        "Is this person wearing any accessories on their face or head?",
        "Does this person have a distinct hair color, such as blonde, red, or mixed?",
        "Does this person have a clean-shaven face?",
        "Does this person appear to have curly or wavy hair?",
        "Is this person bald?",
        "Does this person have lighter-colored eyes, such as blue or green?",
        "Is this person smiling?",
        "Does this person have freckles or dimples?",
        "Is this person male?"
    ]
    for q in questions:
        print(q)
        trait = get_trait_from_question(q)
        print(trait)
        print('-------------')