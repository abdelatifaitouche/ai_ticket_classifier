from fastapi import APIRouter
from src.features.tickets.api.routes import router as ticket_router

router = APIRouter(prefix="/api/v1")


router.include_router(ticket_router)
