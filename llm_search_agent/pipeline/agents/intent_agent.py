from langchain import LLMChain
from langchain.llms import OpenAI
from llm_search_agent.prompt_manager import PromptManager
from llm_search_agent.config import Settings

cfg = Settings()
prompt_mgr = PromptManager()
intent_prompt = prompt_mgr.load("intent_extraction", ["user_question"])

class IntentAgent:
    def __init__(self):
        self.chain = LLMChain(
            llm=OpenAI(
                openai_api_base=cfg.txt_server_url,
                model_name=cfg.intent_model,
                openai_api_key=None,
                temperature=0.0
            ),
            prompt=intent_prompt
        )

    def extract(self, question: str) -> str:
        return self.chain.run(user_question=question).strip()
