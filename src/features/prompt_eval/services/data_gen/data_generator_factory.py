from .model_data_gen import ModelDataGenerator
from src.core.shared.enums.llm_client import LlmClient
from src.infra.llm.claude_client import ClaudeClient
from src.infra.llm.gemini_client import GeminiClient


def get_data_generator(model: LlmClient) -> ModelDataGenerator:
    match model:
        case LlmClient.GEMINI:
            return ModelDataGenerator(client=GeminiClient(), model="gemini-3.5-flash")
        case LlmClient.CLAUDE:
            return ModelDataGenerator(client=ClaudeClient(), model="claude-haiku-4-5")
        case _:
            raise ValueError("No model ")
