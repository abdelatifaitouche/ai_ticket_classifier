import pytest
from src.features.tickets.domain.ticket import Ticket


@pytest.fixture
def ticket():
    return Ticket.create(
        category="BILLING",
        severity="HIGH",
        summary="Charged twice",
        message="I was f ing charged twice ",
    )


class TestTicketCreation:
    def test_success_creation(self, ticket):
        assert ticket.category == "BILLING"
        assert ticket.severity == "HIGH"
        assert len(ticket.summary) > 0
        assert len(ticket.message) > 0
