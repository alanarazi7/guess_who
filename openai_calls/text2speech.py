import pygame
import openai
import tempfile
import os

from openai_calls.constants import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def play_voice(text):
    # Generate speech with OpenAI's Voice API
    response = openai.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    # Save audio to a temporary MP3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(response.content)
        temp_audio_path = temp_audio.name

    # Play audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

    # Clean up the file
    os.remove(temp_audio_path)


if __name__ == "__main__":
    play_voice("Hello, how are you?")