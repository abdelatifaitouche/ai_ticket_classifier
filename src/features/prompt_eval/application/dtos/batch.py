from pydantic import BaseModel, Field, ConfigDict


class Question(BaseModel):
    model_config = ConfigDict(extra="forbid")
    question: str = Field(description="question generate the ai ticket triage")


class QuestionBatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    topic: str = Field(description="the batch topic")
    questions: list[Question] = Field(description="a list of questions generated.")
