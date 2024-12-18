import os
import tempfile

import openai
from openai import OpenAI

from constants import OPENAI_API_KEY, OPENAI_MODEL

openai.api_key = OPENAI_API_KEY


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



def play_voice(text):
    # Generate speech with OpenAI's Voice API
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    # Save audio to a temporary MP3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(response.content)
        temp_audio_path = temp_audio.name

    # Play audio using system's default tool
    os.system(f"afplay {temp_audio_path}")  # macOS-specific, replace for other OS if needed

    # Clean up the file
    os.remove(temp_audio_path)


if __name__ == "__main__":
    answer = ask_openai("Hi, what is your name?")
    print(answer)
    play_voice(answer)