from dataclasses import dataclass


@dataclass(frozen=True)
class TicketCreateRequest:
    message: str
