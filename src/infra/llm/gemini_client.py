from google import genai
from src.core.config import settings
from src.core.llm.base import BaseLLMClient
from typing import Any, Optional


class GeminiClient(BaseLLMClient):
    _instance: Optional["GeminiClient"] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )
        self._initialized = True

    def generate(
        self,
        model: str,
        input: str,
        response_format: dict[str, str] | None = None,
    ):

        config: dict[str, Any] = {
            "model": model,
            "input": input,
        }

        if response_format:
            config["response_format"] = response_format

        return self.client.interactions.create(**config)
