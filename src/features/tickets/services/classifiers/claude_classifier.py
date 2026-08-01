from src.features.tickets.interfaces.classifier import IClassifier
from anthropic import Anthropic
from src.features.tickets.application.dto import TicketClassifierDTO


class ClaudeClassifier(IClassifier):
    def __init__(self, client: Anthropic):
        self._client: Anthropic = client

    def classify(self, message: str):
        PROMPT: str = f"""
        You are a banking ticket assistant, review the user ticket, and classify it based
        On the Category, Severity, and give a summary of the ticket        
        """

        output = self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            system=PROMPT,
            tool_choice={"type": "tool", "name": "TicketClassifierTool"},
            tools=[
                {
                    "name": "TicketClassifierTool",
                    "description": "Classify the ticket content strictly into the schema",
                    "input_schema": TicketClassifierDTO.model_json_schema(),
                },
            ],
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )
        return TicketClassifierDTO.model_validate(output.content[0].input)
