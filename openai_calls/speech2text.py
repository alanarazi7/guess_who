import openai
import sounddevice as sd
import soundfile as sf
import os

from openai_calls.constants import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def record_audio(duration=5, filename="output.wav"):
    print("Recording... Speak now!")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    print("Recording complete!")
    sf.write(filename, audio, 44100)
    return filename

def transcribe_audio(file_path):
    # Use Whisper API for transcription
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="en"
        )
    return transcript.text


def do_speech_to_text(seconds: int = 4):
    # Record and transcribe audio
    audio_file_path = record_audio(duration=seconds)
    transcription = transcribe_audio(audio_file_path)

    print("Transcription:", transcription)

    # Clean up the temporary audio file
    os.remove(audio_file_path)
    return transcription


if __name__ == "__main__":
    do_speech_to_text()
