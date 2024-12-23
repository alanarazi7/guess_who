import tempfile
from typing import Optional

import openai
import os
import streamlit as st

from audio_recorder_streamlit import audio_recorder

from openai_calls.constants import OPENAI_API_KEY, DEBUG_MODE

openai.api_key = OPENAI_API_KEY

def record_message(key: str) -> Optional[str]:
    audio_bytes = audio_recorder(key=f"audio_recorder_{key}")
    if not audio_bytes:
        return None
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name
        transcription = transcribe_audio(temp_audio_path)
        os.remove(temp_audio_path)

    if transcription:
        if DEBUG_MODE:
            st.info(f"Your Answer: {transcription}", icon="🎤")
    else:
        st.error("Transcription failed. Please try again.")

    return transcription

def transcribe_audio(file_path):
    # Use Whisper API for transcription
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="en"
        )
    return transcript.text

