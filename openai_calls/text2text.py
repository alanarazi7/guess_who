from openai import OpenAI

from constants import OPENAI_API_KEY, OPENAI_TEXT_MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def ask_openai(prompt):
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
    answer = ask_openai("Hi, what is your name?")
    print(answer)