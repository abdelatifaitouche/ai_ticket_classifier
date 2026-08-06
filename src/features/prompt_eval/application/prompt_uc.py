from src.features.prompt_eval.domain.prompt import Prompt, PromptVersion
from src.features.prompt_eval.infra.repositories.prompt_repository import (
    PromptRepository,
)
from src.features.prompt_eval.application.commands import CreatePrompt
from sqlalchemy.orm import Session


class PromptUC:
    def __init__(self, repo: PromptRepository, session: Session):
        self.repo: PromptRepository = repo
        self.session: Session = session

    def create_prompt(self, data: CreatePrompt) -> Prompt:

        prompt: Prompt = Prompt.create(
            initial_text=data.text,
            task=data.task,
        )

        prompt: Prompt = self.repo.save(prompt)

        self.session.commit()

        return prompt
