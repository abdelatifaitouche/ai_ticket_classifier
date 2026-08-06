import pytest
import logging
from src.features.prompt_eval.services.data_gen.model_data_gen import ModelDataGenerator
from src.infra.llm.gemini_client import GeminiClient


logger = logging.getLogger(__name__)


class TestDataSetGeneration:
    def test_data_generation(self):
        gen = ModelDataGenerator(GeminiClient())

        data_set = gen.generate(5)

        logger.info(data_set)

        assert len(data_set.questions) == 5
