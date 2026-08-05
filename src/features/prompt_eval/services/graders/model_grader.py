from src.features.prompt_eval.interfaces.grader import IGrader
from pydantic import BaseModel, Field

""" 
This code wont work, its just a placeholder to
strucutre everyting, and get a clean overview on how the
implemenation and interface of the LLM clients should be

"""


class Evaluation(BaseModel):
    question: str = Field(description="question asked")
    answer: str = Field(description="answer got")
    score: int = Field(description="score of the answer of the question from 0-10")


class ModelGrader(IGrader):
    def __init__(self, client):
        self.client = client

    def run(self):
        PROMPT: str = f"""
        Score the answer provided by our ai ticket assistant {interaction.answer} based on the user's question {interaction.question},
        on a scale of 0-10.
        """

        evaluation = self.client.generate(
            model="gemini-3.5-flash",
            input=PROMPT,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": Evaluation.model_json_schema(),
            },
        )

        return Evaluation.model_validate_json(evaluation.output_text)
