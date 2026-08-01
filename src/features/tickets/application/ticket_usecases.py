from src.features.tickets.application.commands import TicketCreateRequest
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from src.features.tickets.domain.ticket import Ticket
from src.features.tickets.interfaces.classifier import IClassifier
from src.features.tickets.interfaces.repository import IRepository
from src.features.tickets.application.dto import TicketClassifierDTO


class TicketUC:
    def __init__(self, session: Session, classifier: IClassifier, repo: IRepository):
        self._classifier: IClassifier = classifier
        self._repo: IRepository = repo
        self._session: Session = session

    def create_ticket(self, data: TicketCreateRequest) -> Ticket:

        output: TicketClassifierDTO = self._classifier.classify(data.message)

        ticket = Ticket.create(
            category=output.category.value,
            severity=output.severity.value,
            summary=output.summary,
            message=data.message,
        )
        ticket = self._repo.save(ticket)

        self._session.commit()

        return ticket
