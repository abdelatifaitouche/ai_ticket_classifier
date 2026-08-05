from abc import ABC, abstractmethod


class BaseLLMClient(ABC):
    @abstractmethod
    def generate(self, *args, **kwargs):
        raise NotImplementedError(
            "Generate method on llm client needs to be implemented"
        )
