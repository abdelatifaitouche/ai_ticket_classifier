from src.core.llm.base import BaseLLMClient

""" 
This code wont work, its just a placeholder to
strucutre everyting, and get a clean overview on how the
implemenation and interface of the LLM clients should be

"""


class ModelDataGenerator:
    def __init__(self, client: BaseLLMClient):
        self.client: BaseLLMClient = client

    def generate(self, test_size: int):
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

        return self.client.generate(
            PROMPT,
            response_format,
        )
