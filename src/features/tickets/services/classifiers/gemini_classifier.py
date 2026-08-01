from src.features.tickets.interfaces.classifier import IClassifier
from google.genai import Client
from src.features.tickets.application.dto import TicketClassifierDTO


class GeminiClassifier(IClassifier):
    def __init__(self, client: Client):
        self.client: Client = client

    def classify(self, message: str) -> TicketClassifierDTO:
        PROMPT: str = f"""
        You are a banking ticket assistant, review the user ticket {message}, and classify it based
        On the Category, Severity, and give a summary of the ticket        
        """
        output = self.client.interactions.create(
            model="gemini-3.5-flash",
            input=PROMPT,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": TicketClassifierDTO.model_json_schema(),
            },
        )

        return TicketClassifierDTO.model_validate_json(output.output_text)
