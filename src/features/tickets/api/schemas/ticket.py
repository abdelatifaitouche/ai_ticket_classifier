from pydantic import BaseModel
from uuid import UUID


class CreateTicket(BaseModel):
    message: str


class TicketRead(BaseModel):
    id: UUID
    category: str
    severity: str
    summary: str
    message: str

    model_config = {"from_attributes": True}
