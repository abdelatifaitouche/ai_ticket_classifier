from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class PromptVersion:
    id: UUID
    prompt_id: UUID
    text: str
    version: int
    is_current: bool
    created_at: datetime

    def __post_init__(self):
        self._validate(self.text)

    @staticmethod
    def _validate(text: str) -> None:
        if not text or text.strip() == "" or len(text) < 20:
            raise ValueError("Prompt text cannot be empty or less than 20 characters")

    @classmethod
    def create(cls, *, prompt_id: UUID, text: str, version: int) -> "PromptVersion":
        return cls(
            id=uuid4(),
            prompt_id=prompt_id,
            text=text,
            version=version,
            is_current=False,
            created_at=datetime.utcnow(),
        )


@dataclass
class Prompt:
    id: UUID
    task: str
    versions: list[PromptVersion] = field(default_factory=list)

    def __post_init__(self):
        current = [v for v in self.versions if v.is_current]
        if len(current) > 1:
            raise ValueError("A prompt can only have one current version")
        if current and current[0] not in self.versions:
            raise ValueError("Current version must be one of this prompt's versions")

    @property
    def current_version(self) -> PromptVersion | None:
        return next((v for v in self.versions if v.is_current), None)

    @classmethod
    def create(cls, *, task: str, initial_text: str) -> "Prompt":
        prompt = cls(id=uuid4(), task=task, versions=[])
        first_version = PromptVersion.create(
            prompt_id=prompt.id, text=initial_text, version=1
        )
        first_version.is_current = True
        prompt.versions.append(first_version)
        return prompt

    def add_candidate(self, text: str) -> PromptVersion:
        next_version_number = len(self.versions) + 1
        candidate = PromptVersion.create(
            prompt_id=self.id, text=text, version=next_version_number
        )
        self.versions.append(candidate)
        return candidate

    def promote(self, candidate: PromptVersion) -> None:
        if candidate not in self.versions:
            raise ValueError(
                "Cannot promote a version that doesn't belong to this prompt"
            )
        for v in self.versions:
            v.is_current = False
        candidate.is_current = True
