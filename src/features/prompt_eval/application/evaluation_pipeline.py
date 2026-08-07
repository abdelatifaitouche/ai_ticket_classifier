from src.features.prompt_eval.interfaces.grader import IGrader
from src.features.prompt_eval.interfaces.data_gen_interface import IDataGenerator
from src.features.prompt_eval.interfaces.qna_interface import IQna
from src.features.prompt_eval.domain.evaluation_run import Evaluation, EvaluationRun
from src.features.prompt_eval.domain.prompt import Prompt, PromptVersion
from src.features.prompt_eval.infra.repositories.prompt_repository import (
    PromptRepository,
)
from uuid import UUID


class EvaluationPipeline:
    def __init__(
        self,
        grader: IGrader,
        data_generator: IDataGenerator,
        qna: IQna,
        prompt_repo: PromptRepository,
    ):
        self._grader: IGrader = grader
        self._data_generator: IDataGenerator = data_generator
        self._qna: IQna = qna
        self._prompt_repo: PromptRepository = prompt_repo

    def setup(self, prompt_id: UUID):

        prompt: Prompt | None = self._prompt_repo.get_by_id(prompt_id)

        if not prompt:
            raise

        questions: list[str] = []
        evaluation: Evaluation = Evaluation.create(
            prompt=prompt,
            questions=questions,
        )

        return

    def execute(self, evaluation: Evaluation, prompt_version: PromptVersion):
        evaluation_run: EvaluationRun = evaluation.execute(prompt_version)

        answers = self._qna.run(evaluation.questions)

        metrics = self._grader.run(evaluation.questions, answers)

        evaluation_run.metrics = metrics

        pass
