import pytest
from pydantic import BaseModel, Field, ConfigDict
from src.infra.llm.claude_client import ClaudeClient
from src.infra.llm.gemini_client import GeminiClient
import logging


logger = logging.getLogger(__name__)

gemini_client = GeminiClient()
claude_client = ClaudeClient()


class Ingredient(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ingredient: str = Field(description="ingredient name and quantity")


class Recipe(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str = Field(description="name of the receipe")
    ingredients: list[Ingredient] = Field(
        description="list of ingredients needed for the receipe"
    )


SYSTEM_PROMPT: str = "You are a masterclass chef, answer this question"


class TestLlmClient:
    def test_gemini_client(self):

        message = "give me a tortila receipe"

        receipe = gemini_client.generate(
            message=message,
            system_prompt=SYSTEM_PROMPT,
            model="gemini-3.5-flash",
            output_shape=Recipe,
        )

        logger.info(receipe)
        assert True

    def test_claude_client(self):
        message = "give me a tortila receipe"

        receipe = claude_client.generate(
            message=message,
            system_prompt=SYSTEM_PROMPT,
            model="claude-haiku-4-5",
            output_shape=Recipe,
        )

        logger.info(receipe)
        assert True
