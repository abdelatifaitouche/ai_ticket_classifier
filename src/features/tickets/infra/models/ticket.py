"""
from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import


class Ticket(Base):
    id
    category
    severity
    summary
    message
    status
    submitted_at
    resolved_at
    updated_at
"""
