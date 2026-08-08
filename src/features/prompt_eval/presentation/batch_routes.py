from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infra.db.session import get_db
from src.features.prompt_eval.application.batch_uc import BatchUC
from src.features.prompt_eval.infra.repositories.batch_repo import BatchRepository
from src.core.shared.enums.llm_client import LlmClient

router = APIRouter(prefix="/batch")


def get_uc(db: Session = Depends(get_db)):
    return BatchUC(BatchRepository(db), db)


@router.post("/")
def create_batch(
    batch_size: int,
    topic: str,
    uc: BatchUC = Depends(get_uc),
):
    batch = uc.create_batch(batch_size=batch_size, topic=topic, model=LlmClient.GEMINI)
    return batch
