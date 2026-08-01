from anthropic import Anthropic
from src.core.config import settings


claude_client = None


def get_claude_client():
    global claude_client

    if not claude_client:
        claude_client = Anthropic(api_key=settings.CLAUDE_API_KEY)

    return claude_client
