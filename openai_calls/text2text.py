import json

from openai import OpenAI

from openai_calls.constants import OPENAI_API_KEY, OPENAI_TEXT_MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def ask_textually(prompt, force_json: bool = False):
    if force_json:
        prompt += f"\n\nAnswer in JSON format."
    kwargs = {'messages': [{'role': 'user', 'content': prompt}], 'model': OPENAI_TEXT_MODEL}
    if force_json:
        kwargs['response_format'] = {"type": "json_object"}
    response = client.chat.completions.create(**kwargs)
    choice = response.choices[0]
    completion = choice.message.content
    if force_json:
        completion = json.loads(completion)
    return completion



if __name__ == "__main__":
    answer = ask_textually("Hi, what is your name?")
    print(answer)
    answer = ask_textually("Hi, what is your name?", force_json=True)
    print(answer)