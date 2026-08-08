from src.core.llm.base import BaseLLMClient
from src.infra.llm.gemini_client import GeminiClient
from src.infra.llm.claude_client import ClaudeClient
from pydantic import BaseModel, Field, ConfigDict
from src.features.prompt_eval.application.dtos.batch import QuestionBatch


class ModelDataGenerator:
    def __init__(self, client: BaseLLMClient, model: str):
        self.client: BaseLLMClient = client
        self.model: str = model

    def generate(self, test_size: int, topic: str) -> QuestionBatch:
        PROMPT: str = f"""
            In the context of {topic}, we need to generate a number {test_size} of questions to test how well
            the main prompt is effective, generate {test_size} questions for this {topic}, the questions should not be the same, nor
            addressing the same issue,
        """
        generated_questions = self.client.generate(
            model=self.model, message=PROMPT, output_shape=QuestionBatch
        )

        return generated_questions
