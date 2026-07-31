from pydantic import BaseModel


class CreateTicket(BaseModel):
    message: str
