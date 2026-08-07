from abc import ABC, abstractmethod
from pydantic import BaseModel


class BaseLLMClient(ABC):
    @abstractmethod
    def generate(
        self,
        message: str,
        model: str,
        output_shape: type[BaseModel],
        system_prompt: str | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ) -> type[BaseModel]:
        raise NotImplementedError(
            "Generate method on llm client needs to be implemented"
        )
