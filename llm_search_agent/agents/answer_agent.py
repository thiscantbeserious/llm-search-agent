from langchain import LLMChain
from langchain.llms import OpenAI
from llm_search_agent.prompt_manager import PromptManager
from llm_search_agent.config import Settings

cfg = Settings()
prompt_mgr = PromptManager()
answer_prompt = prompt_mgr.load("answer_generation", ["user_question","search_results"])

class AnswerAgent:
    def __init__(self):
        self.chain = LLMChain(
            llm=OpenAI(
                openai_api_base=cfg.txt_server_url,
                model_name=cfg.answer_model,
                openai_api_key=None,
                temperature=0.0
            ),
            prompt=answer_prompt
        )

    def generate(self, question: str, results: list[dict]) -> str:
        res_text = "\n\n".join(
            f"{i+1}. {r.get('title')} — {r.get('snippet')} ({r.get('link') or r.get('url')})"
            for i,r in enumerate(results)
        ) or "No results found."
        return self.chain.run(user_question=question, search_results=res_text).strip()
