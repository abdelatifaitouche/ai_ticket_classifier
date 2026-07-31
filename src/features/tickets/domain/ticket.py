from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.tickets.domain.state import Status, Category, Severity
from datetime import datetime


@dataclass
class Ticket:
    id: UUID
    category: Category
    severity: Severity
    summary: str
    message: str
    status: Status
    submitted_at: datetime
    updated_at: datetime
    resolved_at: datetime | None = None

    @classmethod
    def create(cls, *, category, severity, summary, message) -> "Ticket":
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
