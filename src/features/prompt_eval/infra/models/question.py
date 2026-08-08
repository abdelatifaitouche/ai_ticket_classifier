from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, String, ForeignKey, DateTime
import uuid
from datetime import datetime


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    question: Mapped[str] = mapped_column(
        String,
        nullable=True,
    )
    batch_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("questions_batch.id"),
        nullable=True,
    )

    batch: Mapped["Batch"] = relationship(back_populates="questions")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
