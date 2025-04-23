from langchain import LLMChain
from langchain_community.llms import OpenAI
from llm_search_agent.prompt_manager import PromptManager
from llm_search_agent.config import Settings

cfg = Settings()
prompt_mgr = PromptManager()
intent_prompt = prompt_mgr.load("intent_extraction", ["user_question"])


class IntentAgent:
    def __init__(self):
        self.chain = LLMChain(
            llm=OpenAI(
                openai_api_base=cfg.openai_api_url,
                openai_api_key=cfg.openai_api_key,
                model_name=cfg.intent_model,
                temperature=cfg.intent_temperature,
            ),
            prompt=intent_prompt
        )

    def extract(self, question: str) -> str:
        return self.chain.run(user_question=question).strip()
