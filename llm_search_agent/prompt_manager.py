import shutil
from pathlib import Path
from langchain import PromptTemplate

class PromptManager:
    def __init__(
        self,
        base_dir: Path,
        custom_dir_name: str = "prompts",
        default_dir_name: str = "templates",
    ):
        """
        base_dir: project root (where 'prompts/' and 'templates/' live)
        """
        self.custom_dir  = (base_dir / custom_dir_name).resolve()
        self.default_dir = (base_dir / default_dir_name).resolve()

        # Ensure the prompts folder exists
        self.custom_dir.mkdir(parents=True, exist_ok=True)

        # Copy over any missing templates
        for tpl in self.default_dir.glob("*.prompt"):
            dest = self.custom_dir / tpl.name
            if not dest.exists():
                shutil.copy(tpl, dest)

    def load(self, name: str, variables: list[str]) -> PromptTemplate:
        """
        Load `<name>.prompt` from prompts/, raising if somehow missing.
        """
        custom_path = self.custom_dir / f"{name}.prompt"
        if not custom_path.exists():
            raise FileNotFoundError(f"Prompt '{name}.prompt' not found in {self.custom_dir}")
        text = custom_path.read_text(encoding="utf-8")
        return PromptTemplate(template=text, input_variables=variables)