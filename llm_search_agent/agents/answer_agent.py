from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable

from llm_search_agent.llm_loader import load_llm_with_model
from llm_search_agent.prompt_manager import PromptManager
from llm_search_agent.config import Config

cfg = Config()
prompt_mgr = PromptManager()
answer_prompt = prompt_mgr.load("answer_generation", ["user_question", "search_results"])


class AnswerAgent:
    def __init__(self, llm=None):
        # Allow injection (useful for tests), default to our single provider
        self.llm = llm or load_llm_with_model(cfg.answer_model, cfg.answer_temperature)
        self.chain: RunnableSerializable[dict[str, str], str] = (
                answer_prompt | self.llm | StrOutputParser()
        )

    def generate(self, question: str, results: list[dict]) -> str:
        res_text = "\n\n".join(
            f"{i + 1}. {r.get('title')} — {r.get('snippet')} ({r.get('link') or r.get('url')})"
            for i, r in enumerate(results)
        ) or "No results found."
        return self.chain.run(user_question=question, search_results=res_text).strip()
