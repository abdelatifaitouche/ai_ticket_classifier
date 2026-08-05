"""

This Code is just a test to see the overrall workflow how should look like


The goal is to have a prompt, bunch of questions,
then answers of these questions based on the prompt,
each answer gets evaluated/score,
an average is calculated, and loop back til will get an improvement that satisfiys us
"""

from src.infra.llm.gemini_client import get_gemini_client
from pydantic import BaseModel, Field


class Question(BaseModel):
    question: str = Field(description="question generate the ai ticket triage")


class TestUseCase(BaseModel):
    title: str = Field(description="test title.")
    questions: list[Question] = Field(description="a list of questions generated.")


class Interaction(BaseModel):
    prompt: str = Field(description="prompt provided by the system.")
    question: str = Field(description="user asked question.")
    answer: str = Field(description="answer of the prompt given.")


def generate_questions(test_size: int) -> TestUseCase:
    PROMPT: str = f"""
    In the context of an ai ticket triage application, we need to geneerate a number {test_size} of questions to test how well
    the main prompt is effective, generate {test_size} questions for this usecase, the questions should not be the same, nor
    addressing the same issue,
    """
    client = get_gemini_client()

    questions = client.interactions.create(
        model="gemini-3.5-flash",
        input=PROMPT,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": TestUseCase.model_json_schema(),
        },
    )

    return TestUseCase.model_validate_json(questions.output_text)


def qna(questions: TestUseCase) -> list[Interaction]:

    client = get_gemini_client()

    results: list[Interaction] = []

    for question in questions.questions:
        PROMPT: str = f"""
        You are a banking ticket assistant, review the user ticket {question}, and classify it based
        On the Category, Severity, and give a summary of the ticket        
        """

        answer = client.interactions.create(
            model="gemini-3.5-flash",
            input=PROMPT,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": Interaction.model_json_schema(),
            },
        )

        results.append(Interaction.model_validate_json(answer.output_text))

    return results


def eval(interaction: Interaction):

    client = get_gemini_client()

    PROMPT: str = f"""
    Score the answer provided by our ai ticket assistant {interaction.answer} based on the user's question {interaction.question},
    on a scale of 0-10.
    """

    class Evaluation(BaseModel):
        question: str = Field(description="question asked")
        answer: str = Field(description="answer got")
        score: int = Field(description="score of the answer of the question from 0-10")

    evaluation = client.interactions.create(
        model="gemini-3.5-flash",
        input=PROMPT,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": Evaluation.model_json_schema(),
        },
    )

    return Evaluation.model_validate_json(evaluation.output_text)


def workflow(test_size: int):
    print(f"INIT THE WORKFLOW FOR A TEST SUIT OF {test_size} questions.")
    print("Generating test suit ........")

    questions: TestUseCase = generate_questions(test_size)
    print("Test suit Generated ......... OK")
    print("Q&A Started ...........")

    results: list[Interaction] = qna(questions)

    print("Q&A finished ........ OK")
    scores = []
    print("Evaluation started .........")
    for interaction in results:
        scores.append(eval(interaction))
    print("Evaluation Ended ...... OK")
    print("Workflow Finished ...... OK")
    return scores
