from dataclasses import dataclass
from uuid import UUID, uuid4
from .prompt import Prompt, PromptVersion
from .question_batch import QuestionBatch


@dataclass
class EvaluationRun:
    """I think this one should be linked to a prompt version"""

    id: UUID
    prompt_version: PromptVersion
    version: int
    metrics: int


@dataclass
class Evaluation:
    id: UUID
    latest_run: int
    prompt: Prompt
    test_batch: QuestionBatch
    evaluation_executions: list[EvaluationRun] | None

    @classmethod
    def create(
        cls, *, prompt: Prompt, questions: list[str], test_batch: QuestionBatch
    ) -> "Evaluation":
        return cls(
            id=uuid4(),
            prompt=prompt,
            test_batch=test_batch,
            latest_run=0,
            evaluation_executions=[],
        )

    def execute(self, prompt_version: PromptVersion):
        return
