from sqlalchemy.orm import Session
from uuid import UUID
from sqlalchemy import select
from src.features.tickets.infra.models.ticket import Ticket as TicketDB
from src.features.tickets.domain.ticket import Ticket as TicketEntity
from src.features.tickets.interfaces.repository import IRepository


class TicketRepository(IRepository):
    def __init__(self, db: Session):
        self.db: Session = db

    def _to_orm(self, entity: TicketEntity) -> TicketDB:
        return TicketDB(
            id=entity.id,
            category=entity.category,
            severity=entity.severity,
            status=entity.status,
            message=entity.message,
            summary=entity.summary,
            submitted_at=entity.submitted_at,
            resolved_at=entity.resolved_at,
            updated_at=entity.updated_at,
        )

    def _to_domain(self, orm: TicketDB):
        return TicketEntity(
            id=orm.id,
            category=orm.category,
            severity=orm.severity,
            summary=orm.summary,
            message=orm.message,
            status=orm.status,
            submitted_at=orm.submitted_at,
            resolved_at=orm.resolved_at,
            updated_at=orm.updated_at,
        )

    def save(self, entity: TicketEntity) -> TicketEntity:
        orm: TicketDB = self._to_orm(entity)
        self.db.add(orm)
        self.db.flush()
        return entity

    def get_by_id(self, entity_id: UUID) -> TicketEntity | None:
        stmt = select(TicketDB).where(TicketDB.id == entity_id)

        result = (self.db.execute(stmt)).scalar_one_or_none()

        if not result:
            return None

        return self._to_domain(result)

    def update(self):
        return

    def delete(self):
        return
