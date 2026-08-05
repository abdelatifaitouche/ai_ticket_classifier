from src.features.prompt_eval.interfaces.qna_interface import IQna
from src.core.llm.base import BaseLLMClient

""" 
This code wont work, its just a placeholder to
strucutre everyting, and get a clean overview on how the
implemenation and interface of the LLM clients should be

"""


class ModelQna(IQna):
    def __init__(self, client: BaseLLMClient):
        self.client: BaseLLMClient = client

    def run(self, questions: list):
        results: list[Interaction] = []

        for question in questions.questions:
            PROMPT: str = f"""
            You are a banking ticket assistant, review the user ticket {question}, and classify it based
            On the Category, Severity, and give a summary of the ticket        
            """

            answer = client.interactions.create(
                model="gemini-3.5-flash",
                input=PROMPT,
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": Interaction.model_json_schema(),
                },
            )

            results.append(Interaction.model_validate_json(answer.output_text))

        return results
