import openai
import pyaudio
import wave
import tempfile
import os

from openai_calls.constants import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def record_audio(duration=5):
    # Record audio from microphone
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording... Speak now!")
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording complete!")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save recorded audio to a temporary WAV file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return temp_file.name

def transcribe_audio(file_path):
    # Use Whisper API for transcription
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text


def do_speech_to_text():
    # Record and transcribe audio
    audio_file_path = record_audio(duration=5)
    transcription = transcribe_audio(audio_file_path)

    print("Transcription:", transcription)

    # Clean up the temporary audio file
    os.remove(audio_file_path)
    return transcription


if __name__ == "__main__":
    do_speech_to_text()
