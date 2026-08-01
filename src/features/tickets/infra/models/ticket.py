from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, DateTime, String
import uuid
from datetime import datetime
from src.features.tickets.domain.state import Status, Severity, Category


class Ticket(Base):
    __tablename__ = "tickets"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    category: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    severity: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    summary: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )
    message: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    status: Mapped[str] = mapped_column(String, nullable=False)
    submitted_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
    resolved_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(),
        nullable=False,
    )
