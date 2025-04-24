from langchain_community.utilities import SearxSearchWrapper
from llm_search_agent.config import Config

cfg = Config()
search_tool = SearxSearchWrapper(
    searx_host=cfg.searxng_url,
    unsecure=True
)


class SearchAgent:
    def __init__(self):
        self.tool = search_tool
        self.max_depth = cfg.max_depth
        self.max_width = cfg.max_width

    def search(self, intent: str) -> list[dict]:
        visited = set([intent.lower()])
        queue = [(intent, 0)]
        all_hits = []
        while queue and len(visited) < self.max_depth:
            q, depth = queue.pop(0)
            hits = self.tool.results(q, num_results=self.max_width)
            all_hits.extend(hits)
            if depth < self.max_depth:
                suggestions = getattr(self.tool, "_result", {}).get("suggestions", [])
                for s in suggestions:
                    sv = s.strip().lower()
                    if sv and sv not in visited:
                        visited.add(sv)
                        queue.append((sv, depth + 1))
        return all_hits
