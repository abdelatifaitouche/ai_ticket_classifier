from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, String, DateTime
from datetime import datetime

import uuid


class Batch(Base):
    __tablename__ = "questions_batch"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    topic: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    questions: Mapped[list["Question"]] = relationship(
        back_populates="batch", cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
