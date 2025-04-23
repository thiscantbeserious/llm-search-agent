from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable

from llm_search_agent.llm.openai import get_openai_llm
from llm_search_agent.prompt_manager import PromptManager
from llm_search_agent.config import Settings

# Load your settings and prompt
cfg: Settings = Settings()
prompt_mgr: PromptManager = PromptManager()
intent_prompt: PromptTemplate = prompt_mgr.load("intent_extraction", ["user_question"])


class IntentAgent:
    def __init__(self, llm=None):
        # Allow injection (useful for tests), default to our single provider
        self.llm = llm or get_openai_llm()
        self.chain: RunnableSerializable[dict[str, str], str] = (
                intent_prompt | self.llm | StrOutputParser()
        )

    def extract(self, question: str) -> str:
        # Invoke the sequence with a dict of inputs
        result = self.chain.invoke({"user_question": question})
        # Strip any leading/trailing whitespace
        return result.strip()
