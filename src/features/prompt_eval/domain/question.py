from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Question:
    id: UUID
    text: str

    @classmethod
    def create(cls, *, text: str) -> "Question":
        return cls(
            id=uuid4(),
            text=text,
        )
