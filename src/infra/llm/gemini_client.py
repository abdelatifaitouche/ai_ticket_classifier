from google import genai
from src.core.config import settings
from src.core.llm.base import BaseLLMClient
from typing import Any, Optional
from pydantic import BaseModel


class GeminiClient(BaseLLMClient):
    _instance: Optional["GeminiClient"] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False

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
        message: str,
        model: str,
        output_shape: type[BaseModel],
        system_prompt: str | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ) -> BaseModel:

        response_format = {
            "type": "text",
            "mime_type": "application/json",
            "schema": output_shape.model_json_schema(),
        }

        config: dict[str, Any] = {
            "model": model,
            "input": message,
            "response_format": response_format,
        }

        if system_prompt:
            config["system_instruction"] = system_prompt

        output = self.client.interactions.create(**config)

        return output_shape.model_validate_json(output.output_text)
