from sqlalchemy.orm import Session
from src.features.prompt_eval.infra.models.prompt import Prompt as PromptDB
from src.features.prompt_eval.infra.models.prompt_version import (
    PromptVersion as PromptVersionDB,
)
from src.features.prompt_eval.domain.prompt import Prompt, PromptVersion
from uuid import UUID


class PromptRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def save(self, prompt: Prompt) -> Prompt:

        prompt_orm: PromptDB = PromptDB(
            id=prompt.id,
            task=prompt.task,
        )
        prompt_versions_orm: list[PromptVersionDB] = [
            PromptVersionDB(
                id=p_version.id,
                prompt_text=p_version.text,
                version=p_version.version,
                is_current=p_version.is_current,
                created_at=p_version.created_at,
                prompt_id=p_version.prompt_id,
            )
            for p_version in prompt.versions
        ]

        self.session.add_all(
            [
                prompt_orm,
                *prompt_versions_orm,
            ]
        )

        self.session.flush()
        return prompt
