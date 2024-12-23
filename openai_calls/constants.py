import os

import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_TEXT_MODEL = "gpt-4o-mini-2024-07-18"


openai.api_key = OPENAI_API_KEY
DEBUG_MODE = False