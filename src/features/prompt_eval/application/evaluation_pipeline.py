from src.features.prompt_eval.interfaces.grader import IGrader
from src.features.prompt_eval.interfaces.data_gen_interface import IDataGenerator
from src.features.prompt_eval.interfaces.qna_interface import IQna


class EvaluationPipeline:
    def __init__(self, grader: IGrader, data_generator: IDataGenerator, qna: IQna):
        self._grader: IGrader = grader
        self._data_generator: IDataGenerator = data_generator
        self._qna: IQna = qna

    def execute(self):
        """
        Entry point for the Prompt Evaluation Pipeline,

        Overrall logic for this:
            generate a bunch of questions or fetch some prev users questions from the database

            pass them thru an llm with a predefined PROMPT that we want to evaluate,
            get the answers

            pass the question/answers to a grader (either a model grader, code grader or a human grader)
            get the overrall average score,

            update the MAIN prompt to and check the score update

        Args:
            not yet known

        Returns:
            not yet known
        """
        data = self._data_generator.generate()

        answers = self._qna.run()

        grades = self._grader.run()

        return
