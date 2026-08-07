from src.features.prompt_eval.interfaces.data_gen_interface import IDataGenerator
from src.features.prompt_eval.domain.question_batch import QuestionBatch
from src.features.prompt_eval.domain.question import Question


class BatchUC:
    def __init__(self, data_gen: IDataGenerator, repo):
        """
        for the data generator am a bit skiptical rn, maybe it should be a data source where
        its up to the user to choose either to select questions for the batch from somewhere
        or to generate them
        """
        self._data_gen: IDataGenerator = data_gen
        self._repo = repo

    def create_batch(self, batch_size: int, topic: str):

        generated_batch = self._data_gen.generate(test_size=batch_size, topic=topic)

        batch = QuestionBatch.create(topic=topic)

        batch = self._repo.save(batch)

        return batch
