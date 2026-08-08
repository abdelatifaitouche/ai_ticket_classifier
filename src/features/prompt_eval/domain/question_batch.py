from dataclasses import dataclass
from .question import Question
from uuid import UUID, uuid4


@dataclass
class QuestionBatch:
    id: UUID
    topic: str
    questions: list[Question]

    @classmethod
    def create(cls, *, topic: str, questions: list[Question]) -> "QuestionBatch":
        return cls(
            id=uuid4(),
            topic=topic,
            questions=questions,
        )
