class FilterAgent:
    def filter(self, results: list[dict]) -> list[dict]:
        seen = set()
        out = []
        for r in results:
            url = r.get("link") or r.get("url")
            if url and url not in seen:
                seen.add(url)
                out.append(r)
        return out
