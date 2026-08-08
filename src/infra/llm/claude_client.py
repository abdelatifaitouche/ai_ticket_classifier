from anthropic import Anthropic
from src.core.config import settings
from src.core.llm.base import BaseLLMClient
from typing import Any
from pydantic import BaseModel

claude_client = None


class ClaudeClient(BaseLLMClient):
    _instance = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False

        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._client = Anthropic(
            api_key=settings.CLAUDE_API_KEY,
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
        messages = {
            "role": "user",
            "content": message,
        }

        output_config = {
            "format": {
                "type": "json_schema",
                "schema": output_shape.model_json_schema(),
            },
        }

        if not max_tokens:
            max_tokens = 512

        if not temperature:
            temperature = 0.2

        config: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [
                messages,
            ],
            "output_config": output_config,
        }

        if system_prompt:
            config["system"] = system_prompt

        output = self._client.messages.create(
            **config,
        )

        raw = output.content[0].text

        return output_shape.model_validate_json(raw)


def get_claude_client():
    global claude_client

    if not claude_client:
        claude_client = Anthropic(api_key=settings.CLAUDE_API_KEY)

    return claude_client
