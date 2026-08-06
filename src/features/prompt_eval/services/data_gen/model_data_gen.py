from src.core.llm.base import BaseLLMClient
from pydantic import BaseModel, Field

""" 
This code wont work, its just a placeholder to
strucutre everyting, and get a clean overview on how the
implemenation and interface of the LLM clients should be

"""


class Question(BaseModel):
    question: str = Field(description="question generate the ai ticket triage")


class TestUseCase(BaseModel):
    title: str = Field(description="test title.")
    questions: list[Question] = Field(description="a list of questions generated.")


class ModelDataGenerator:
    def __init__(self, client: BaseLLMClient):
        self.client: BaseLLMClient = client

    def generate(self, test_size: int) -> TestUseCase:
        PROMPT: str = f"""
            In the context of an ai ticket triage application, we need to geneerate a number {test_size} of questions to test how well
            the main prompt is effective, generate {test_size} questions for this usecase, the questions should not be the same, nor
            addressing the same issue,
        """

        response_format = (
            {
                "type": "text",
                "mime_type": "application/json",
                "schema": TestUseCase.model_json_schema(),
            },
        )
        generated_questions = self.client.generate(
            model="gemini-3.5-flash",
            input=PROMPT,
            response_format=response_format,
        )

        return TestUseCase.model_validate_json(generated_questions.output_text)
