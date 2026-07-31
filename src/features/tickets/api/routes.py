from fastapi import APIRouter, Depends
from src.features.tickets.api.schemas.ticket import CreateTicket

router = APIRouter(prefix="/tickets")


@router.post("/")
def submit_ticket(ticket_request: CreateTicket):
    return
