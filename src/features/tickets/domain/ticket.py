from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.tickets.domain.state import Status, Category, Severity
from datetime import datetime


@dataclass
class Ticket:
    id: UUID
    category: str
    severity: str
    summary: str
    message: str
    status: str
    submitted_at: datetime
    updated_at: datetime
    resolved_at: datetime | None = None

    @classmethod
    def create(
        cls, *, category: str, severity: str, summary: str, message: str
    ) -> "Ticket":
        cls._validate(summary, message)

        ticket = cls(
            id=uuid4(),
            category=category,
            severity=severity,
            summary=summary,
            message=message,
            status=Status.SUBMITTED,
            submitted_at=datetime.now(),
            updated_at=datetime.now(),
        )
        return ticket

    @classmethod
    def _validate(cls, summary: str, message: str):
        if not summary or summary.strip() == "":
            raise ValueError("Summary message cannot be empty")

        if not message or message.strip() == "":
            raise ValueError("Message cannot be empty")
