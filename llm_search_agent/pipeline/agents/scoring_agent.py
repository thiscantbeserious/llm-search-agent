class ScoringAgent:
    def score(self, results: list[dict]) -> list[dict]:
        scored = []
        for r in results:
            base = r.get("score", 0.5)
            scored.append({**r, "score": base})
        return sorted(scored, key=lambda x: x["score"], reverse=True)
