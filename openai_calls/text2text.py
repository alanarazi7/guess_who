from openai import OpenAI

from openai_calls.constants import OPENAI_API_KEY, OPENAI_TEXT_MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def ask_textually(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=OPENAI_TEXT_MODEL,
    )
    choice = response.choices[0]
    return choice.message.content



if __name__ == "__main__":
    answer = ask_textually("Hi, what is your name?")
    print(answer)