from pydantic import BaseModel, Field
from src.features.tickets.domain.state import Category, Severity


class TicketClassifierDTO(BaseModel):
    category: Category = Field(description="the category of the user ticket")
    severity: Severity = Field(description="the severity of the user ticket")
    summary: str = Field(description="A summary of the user ticket message")
