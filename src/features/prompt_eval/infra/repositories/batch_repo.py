from sqlalchemy.orm import Session
from src.features.prompt_eval.domain.question_batch import QuestionBatch
from src.features.prompt_eval.domain.question import Question
from src.features.prompt_eval.infra.models.batch import Batch as BatchDB
from src.features.prompt_eval.infra.models.question import Question as QuestionDB


class BatchRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def save(self, batch: QuestionBatch) -> QuestionBatch:

        batch_db: BatchDB = BatchDB(
            id=batch.id,
            topic=batch.topic,
        )

        questions: list[QuestionDB] = [
            QuestionDB(
                id=q.id,
                question=q.text,
                batch_id=batch.id,
            )
            for q in batch.questions
        ]

        self.session.add_all(
            [batch_db, *questions],
        )
        self.session.flush()
        return batch
