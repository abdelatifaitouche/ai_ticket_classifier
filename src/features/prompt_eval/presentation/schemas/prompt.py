from pydantic import BaseModel


class PromptCreateRequest(BaseModel):
    text: str
    task: str
