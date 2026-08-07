from dataclasses import dataclass
from .question import Question
from uuid import UUID


@dataclass
class QuestionBatch:
    id: UUID
    topic: str
    questions: list[Question]

    @classmethod
    def create(cls, *, topic: str):
        return
