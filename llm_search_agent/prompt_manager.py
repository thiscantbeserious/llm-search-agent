from pathlib import Path
from langchain import PromptTemplate

class PromptManager:
    def __init__(self, custom_dir="prompts", default_dir="templates"):
        self.custom_dir = Path(custom_dir)
        self.default_dir = Path(default_dir)

    def load(self, name: str, variables: list[str]) -> PromptTemplate:
        filename = f"{name}.prompt"
        custom = self.custom_dir / filename
        default = self.default_dir / filename
        if custom.exists():
            text = custom.read_text(encoding="utf-8")
        else:
            text = default.read_text(encoding="utf-8")
        return PromptTemplate(template=text, input_variables=variables)
