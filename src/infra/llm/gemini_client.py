from google import genai
from src.core.config import settings

gemini_client = None


def get_gemini_client():
    global gemini_client

    if not gemini_client:
        gemini_client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

    return gemini_client
