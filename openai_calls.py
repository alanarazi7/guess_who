from openai import OpenAI

from constants import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model=OPENAI_MODEL,
)

def ask_openai(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )
    choice = response.choices[0]
    return choice.message.content



if __name__ == "__main__":
    answer = ask_openai("Hi, what is your name?")
    print(answer)