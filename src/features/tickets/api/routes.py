from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.features.tickets.api.schemas.ticket import CreateTicket, TicketRead
from src.features.tickets.services.classifiers.gemini_classifier import GeminiClassifier
from src.infra.llm.gemini_client import get_gemini_client, GeminiClient
from src.features.tickets.application.ticket_usecases import TicketUC
from src.infra.db.session import get_db
from src.features.tickets.infra.repostories.ticket_repository import TicketRepository
from src.features.tickets.application.commands import TicketCreateRequest
from src.features.tickets.domain.ticket import Ticket
from src.features.tickets.services.classifiers.claude_classifier import ClaudeClassifier
from src.infra.llm.claude_client import get_claude_client
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/tickets")


def get_uc(session: Session = Depends(get_db)):
    repo: TicketRepository = TicketRepository(session)
    classifier: ClaudeClassifier = ClaudeClassifier(get_claude_client())
    return TicketUC(session, classifier, repo)


@router.post("/")
def submit_ticket(ticket_request: CreateTicket, uc: TicketUC = Depends(get_uc)):

    ticket: Ticket = uc.create_ticket(
        TicketCreateRequest(message=ticket_request.message)
    )

    return TicketRead.model_validate(ticket)
