from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.features.prompt_eval.presentation.schemas.prompt import PromptCreateRequest
from src.features.prompt_eval.application.prompt_uc import PromptUC
from src.features.prompt_eval.infra.repositories.prompt_repository import (
    PromptRepository,
)
from src.infra.db.session import get_db
from src.features.prompt_eval.application.commands import CreatePrompt
from uuid import UUID

router = APIRouter(prefix="/prompt")


def get_uc(db: Session = Depends(get_db)) -> PromptUC:
    repo: PromptRepository = PromptRepository(db)
    return PromptUC(repo, db)


@router.post("/")
def create_prompt(
    data: PromptCreateRequest,
    uc: PromptUC = Depends(get_uc),
):
    prompt = uc.create_prompt(
        CreatePrompt(
            text=data.text,
            task=data.task,
        ),
    )
    return prompt


@router.get("/{prompt_id}")
def get_prompt_by_id(
    prompt_id: UUID,
    uc: PromptUC = Depends(get_uc),
):
    return uc.get_prompt_by_id(prompt_id)
