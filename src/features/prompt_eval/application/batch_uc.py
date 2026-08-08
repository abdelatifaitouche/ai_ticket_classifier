from src.features.prompt_eval.interfaces.data_gen_interface import IDataGenerator
from src.features.prompt_eval.domain.question_batch import (
    QuestionBatch as QuestionBatchEntity,
)
from src.features.prompt_eval.domain.question import Question as QuestionEntity
from src.features.prompt_eval.services.data_gen.data_generator_factory import (
    get_data_generator,
)
from src.core.shared.enums.llm_client import LlmClient
from src.features.prompt_eval.application.dtos.batch import QuestionBatch, Question


class BatchUC:
    def __init__(self, repo, session):
        self._repo = repo
        self.session = session

    def create_batch(self, batch_size: int, topic: str, model: LlmClient):
        generated_batch: QuestionBatch = get_data_generator(model).generate(
            batch_size, topic
        )

        batch = QuestionBatchEntity.create(
            topic=topic,
            questions=[
                QuestionEntity.create(
                    text=q.question,
                )
                for q in generated_batch.questions
            ],
        )

        batch = self._repo.save(batch)

        self.session.commit()
        return batch
