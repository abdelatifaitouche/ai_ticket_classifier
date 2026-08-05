from anthropic import Anthropic
from src.core.config import settings
from src.core.llm.base import BaseLLMClient
from typing import Any

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
        messages: list[dict[str, Any]],
        system_prompt: str | None,
        max_tokens: int = 512,
        temperature: float = 0.2,
        model: str = "claude-sonnet-4.6",
        tool_choice: dict[str, str] | None = None,
        tools: list[dict[str, Any]] | None = None,
    ):
        config: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages,
        }

        if tool_choice:
            if tools:
                config["tool_choice"] = tool_choice
                config["tools"] = tools

        if system_prompt:
            config["system"] = system_prompt

        output = self._client.messages.create(
            **config,
        )

        return output


def get_claude_client():
    global claude_client

    if not claude_client:
        claude_client = Anthropic(api_key=settings.CLAUDE_API_KEY)

    return claude_client
