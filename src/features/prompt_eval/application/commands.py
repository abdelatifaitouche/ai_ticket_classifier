from dataclasses import dataclass


@dataclass(frozen=True)
class CreatePrompt:
    text: str
    task: str
