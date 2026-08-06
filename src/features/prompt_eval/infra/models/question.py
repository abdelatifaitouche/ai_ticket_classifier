from src.infra.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID,String

class Question(Base):
    __tablename__ = "questions"

    id : Mapped[] = mapped_column()
    question : Mapped[] = mapped_column()
