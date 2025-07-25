from smolagents import LiteLLMModel, CodeAgent, DuckDuckGoSearchTool, WikipediaSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API"),
)

class Agent:
    def __init__(self, model=model):
        self.agent = CodeAgent(
            tools=[],
            model=model,
            additional_authorized_imports=['pandas', 'numpy', 'csv', 'PIL', 're', 'json'],
            max_steps=2
        )
        self.agent_prompt = """
                                You are a quiz master.
                                You will be given a topic, generate concise question in this field.
                                Return 3 outputs as JSON:
                                1. question as string, named as "question" in lowercase
                                2. list of 4 answers, just answers, named as "answers" in lowercase
                                3. correct answer, for example A as first answer, named as "correct_answer" in lowercase
                                Example:
                                ['question': 'What is the capital of France?', 'answers': ['Paris', 'London', 'Berlin', 'Rome'], 'correct_answer': 'Paris']
                                Topic of quiz: {topic}
                        """
    def __call__(self, prompt: str):
        task = self.agent_prompt.format(topic=prompt)
        answer = self.agent.run(task)
        return answer


if __name__ == "__main__":
    agent = Agent(model=model)
    answer = agent("Machine Learning")
    print(f"question: {answer['question']}")
    print(f"answers: {answer['answers']}")
    print(f"correct answer: {answer['correct_answer']}")

