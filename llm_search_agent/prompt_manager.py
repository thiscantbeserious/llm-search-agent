import shutil
from langchain_core.prompts import PromptTemplate

from llm_search_agent.constants import PROMPT_DIR, TEMPLATE_DIR


class PromptManager:
    def __init__(
        self
    ):
        self.prompt_dir  = PROMPT_DIR.resolve()
        self.template_dir = TEMPLATE_DIR.resolve()

        # Ensure the prompts folder exists
        self.prompt_dir.mkdir(parents=True, exist_ok=True)

        # Copy over any missing templates
        for tpl in self.template_dir.glob("*.prompt"):
            dest = self.prompt_dir / tpl.name
            if not dest.exists():
                shutil.copy(tpl, dest)

    def load(self, name: str, variables: list[str]) -> PromptTemplate:
        """
        Load `<name>.prompt` from prompts/, raising if somehow missing.
        """
        custom_path = self.prompt_dir / f"{name}.prompt"
        if not custom_path.exists():
            raise FileNotFoundError(f"Prompt '{name}.prompt' not found in {self.prompt_dir}")
        text = custom_path.read_text(encoding="utf-8")
        return PromptTemplate(template=text, input_variables=variables)