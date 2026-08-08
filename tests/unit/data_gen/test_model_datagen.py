import pytest
from src.features.prompt_eval.services.data_gen.data_generator_factory import (
    get_data_generator,
)
from src.core.shared.enums.llm_client import LlmClient
import logging

logger = logging.getLogger(__name__)


class TestDataGenerator:
    def test_gemini_data_generation(self):

        generated = get_data_generator(LlmClient.GEMINI).generate(
            test_size=5, topic="banking system"
        )

        logger.info(generated)

        assert True

    def test_claude_data_generation(self):
        generated = get_data_generator(LlmClient.CLAUDE).generate(
            test_size=5, topic="banking system"
        )

        logger.info(generated)

        assert True
