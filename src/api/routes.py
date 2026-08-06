from fastapi import APIRouter
from src.features.tickets.api.routes import router as ticket_router
from src.features.prompt_eval.presentation.routes import router as prompt_router

router = APIRouter(prefix="/api/v1")


router.include_router(ticket_router)
router.include_router(prompt_router)
