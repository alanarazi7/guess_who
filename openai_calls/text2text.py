import json

from openai import OpenAI

from openai_calls.constants import OPENAI_API_KEY, OPENAI_TEXT_MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

SYS_MSG = '''You are an AI playing guess-who with a small kid. In your answer, try to be fun, encouraging and engaging.
Your answers should always be concise and clear.'''


def ask_textually(prompt, force_json: bool = False):
    if force_json:
        prompt += f"\n\nAnswer in JSON format."
    messages = [{'role': 'system', 'content': SYS_MSG}, {'role': 'user', 'content': prompt}]
    kwargs = {'messages': messages, 'model': OPENAI_TEXT_MODEL}
    if force_json:
        kwargs['response_format'] = {"type": "json_object"}
    response = client.chat.completions.create(**kwargs)
    choice = response.choices[0]
    completion = choice.message.content
    if force_json:
        completion = json.loads(completion)
    return completion
